from ..bit8.common import *
from ..helper import create_func, inplace_to_stable
from ..bit8.blocks import IfZero, IfNotZero
from ..bit8.cmp import Lt, Lte, Eq
from ..bit8.math import FullAdder, Inc, Dec, Add, Mul, HalfAdderInplace, AddInplace
from ..bit8.loop import For

def Add32(circuit, out, a, b):
    carry_in = circuit.shared_var("ADD32_CARRY_IN", 1)
    carry_out = circuit.shared_var("ADD32_CARRY_OUT", 1)
    Clear(circuit, carry_in)
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_out, carry_in)

def MacWithCarry(circuit, out, carry, a, b, c):
    hi = circuit.shared_var("MAC_WITH_CARRY_HI", 1)
    temp = circuit.shared_var("MAC_WITH_CARRY_TEMP", 1)
    Mul(circuit, hi, out, a, b)
    HalfAdderInplace(circuit, out, temp, c)
    AddInplace(circuit, hi, temp)
    HalfAdderInplace(circuit, out, temp, carry)
    AddInplace(circuit, hi, temp)
    Copy(circuit, hi, carry)

def AddWithCarry(circuit, a, carry, b):
    hi = circuit.shared_var("ADD_WITH_CARRY_HI", 1)
    carry2 = circuit.shared_var("ADD_WITH_CARRY_CARRY2", 1)
    HalfAdderInplace(circuit, a, hi, b)
    HalfAdderInplace(circuit, a, carry2, carry)
    AddInplace(circuit, hi, carry2)
    Copy(circuit, hi, carry)


def Mul32(circuit, out, a, b):
    temp = circuit.shared_var("MUL32_TEMP", 1)
    carry = circuit.shared_var("MUL32_CARRY", 1)
    for i in range(4):
        Clear(circuit, carry)
        for j in range(4):
            Copy(circuit, out[i+j], temp)
            MacWithCarry(circuit, out[i+j], carry, a[i], b[j], temp)
        Copy(circuit, carry, out[i+4])

def Inc32(circuit, a):
    carry = circuit.shared_var("INC32", 1)
    Inc(circuit, a[0])
    Eq(circuit, carry, a[0], Const(circuit, 0))
    for i in range(1, 4):
        with IfNotZero(circuit, carry):
            Inc(circuit, a[i])
            Eq(circuit, carry, a[i], Const(circuit, 0))

def Dec32(circuit, a):
    borrow = circuit.shared_var("DEC32", 1)
    Dec(circuit, a[0])
    Eq(circuit, borrow, a[0], Const(circuit, 255))
    for i in range(1, 4):
        with IfNotZero(circuit, borrow):
            Dec(circuit, a[i])
            Eq(circuit, borrow, a[i], Const(circuit, 255))
