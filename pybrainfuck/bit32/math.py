from ..bit8.common import *
from ..helper import create_func, inplace_to_stable
from ..bit8.blocks import IfZero, IfNotZero
from ..bit8.cmp import Lt, Lte, Eq
from ..bit8.math import FullAdder, Inc, Dec, Add, Mul, HalfAdderInplace, AddInplace, BitwiseNotInplace
from ..bit8.loop import For
from ..bit8.io import PrintString
from .common import *

def Add32(circuit, out, a, b):
    carry_in = circuit.alloc(1)
    carry_out = circuit.alloc(1)
    carry_in.clear()
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_in, carry_out)
    carry_in.free()
    carry_out.free()

def Sub32(circuit, out, a, b):
    b_copy = circuit.alloc(4)
    Copy32(circuit, b_copy, b)
    Neg32Inplace(circuit, b_copy)
    Add32(circuit, out, a, b_copy)

def Neg32Inplace(circuit, out):
    for i in range(4):
        BitwiseNotInplace(circuit, out[i])
    Inc32(circuit, out)

def MacWithCarry(circuit, out, carry, a, b, c):
    hi = circuit.alloc(1)
    temp = circuit.alloc(1)
    Mul(circuit, hi, out, a, b)
    HalfAdderInplace(circuit, out, temp, c)
    AddInplace(circuit, hi, temp)
    HalfAdderInplace(circuit, out, temp, carry)
    AddInplace(circuit, hi, temp)
    Copy(circuit, carry, hi)
    hi.free()
    temp.free()


def Mul32(circuit, out, a, b):
    temp = circuit.alloc(1)
    carry = circuit.alloc(1)
    for i in range(4):
        carry.clear()
        for j in range(4):
            Copy(circuit, temp, out[i+j])
            MacWithCarry(circuit, out[i+j], carry, a[i], b[j], temp)
        Copy(circuit, out[i+4], carry)
    temp.free()
    carry.free()

def MulDecimal(circuit, z, x, y):
    result = circuit.alloc(8)
    Mul32(circuit, result, x, y)
    for i in range(4):
        Copy(circuit, z[i], result[2 + i])

def RecipDecimal(circuit, y, x):
    Put32(circuit, y, 0x00010000)
    two = circuit.alloc_const32(0x00020000)
    temp1 = circuit.alloc(4)
    temp2 = circuit.alloc(4)
    i = circuit.alloc(1)
    with For(circuit, i, 20):
        MulDecimal(circuit, temp1, y, x)
        Sub32(circuit, temp2, two, temp1)
        MulDecimal(circuit, temp1, y, temp2)
        Copy32(circuit, y, temp1)

def Inc32(circuit, a):
    carry = circuit.alloc(1)
    zero = circuit.alloc_const8(0)
    Inc(circuit, a[0])
    Eq(circuit, carry, a[0], zero)
    for i in range(1, 4):
        with IfNotZero(circuit, carry):
            Inc(circuit, a[i])
            Eq(circuit, carry, a[i], zero)
    carry.free()
    zero.free()

def Dec32(circuit, a):
    borrow = circuit.alloc(1)
    const = circuit.alloc_const8(255)
    Dec(circuit, a[0])
    Eq(circuit, borrow, a[0], const)
    for i in range(1, 4):
        with IfNotZero(circuit, borrow):
            Dec(circuit, a[i])
            Eq(circuit, borrow, a[i], const)
    borrow.free()
