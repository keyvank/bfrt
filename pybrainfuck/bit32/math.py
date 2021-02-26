from ..bit8.common import *
from ..helper import create_func, inplace_to_stable
from ..bit8.blocks import IfZero, IfNotZero
from ..bit8.cmp import Lt, Lte, Eq
from ..bit8.math import FullAdder, Inc, Dec, Add, Mul, HalfAdderInplace, AddInplace
from ..bit8.loop import For

def Add32(circuit, out, a, b):
    carry_in = circuit.alloc(1)
    carry_out = circuit.alloc(1)
    carry_in.clear()
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_out, carry_in)
    carry_in.free()
    carry_out.free()

def MacWithCarry(circuit, out, carry, a, b, c):
    hi = circuit.alloc(1)
    temp = circuit.alloc(1)
    Mul(circuit, hi, out, a, b)
    HalfAdderInplace(circuit, out, temp, c)
    AddInplace(circuit, hi, temp)
    HalfAdderInplace(circuit, out, temp, carry)
    AddInplace(circuit, hi, temp)
    Copy(circuit, hi, carry)
    hi.free()
    temp.free()

def AddWithCarry(circuit, a, carry, b):
    hi = circuit.alloc(1)
    carry2 = circuit.alloc(1)
    HalfAdderInplace(circuit, a, hi, b)
    HalfAdderInplace(circuit, a, carry2, carry)
    AddInplace(circuit, hi, carry2)
    Copy(circuit, hi, carry)
    hi.free()
    carry2.free()


def Mul32(circuit, out, a, b):
    temp = circuit.alloc(1)
    carry = circuit.alloc(1)
    for i in range(4):
        carry.clear()
        for j in range(4):
            Copy(circuit, out[i+j], temp)
            MacWithCarry(circuit, out[i+j], carry, a[i], b[j], temp)
        Copy(circuit, carry, out[i+4])
    temp.free()
    carry.free()

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
