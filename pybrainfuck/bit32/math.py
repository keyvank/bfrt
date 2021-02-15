from ..bit8.common import *
from ..helper import create_func, inplace_to_stable
from ..bit8.loop import IfZero, IfNotZero
from ..bit8.cmp import Lt, Lte, Eq
from ..bit8.math import FullAdder, Inc, Dec

def Add32(circuit, out, a, b):
    carry_in = circuit.shared_var("ADD32_CARRY_IN", 1)
    carry_out = circuit.shared_var("ADD32_CARRY_OUT", 1)
    Clear(circuit, carry_in)
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_out, carry_in)

def Mul32(circuit, out, a, b):
    pass

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
