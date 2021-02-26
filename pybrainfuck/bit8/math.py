from .common import *
from ..helper import create_func, inplace_to_stable
from .blocks import IfZero, IfNotZero
from .cmp import Lt, Lte

AddInplace = create_func(
    ["x", "y"], [("temp0", 1)],
    """
        temp0[-]
        y[x+temp0+y-]
        temp0[y+temp0-]
    """
)

Add = inplace_to_stable(AddInplace)

SubInplace = create_func(
    ["x", "y"], [("temp0", 1)],
    """
        temp0[-]
        y[x-temp0+y-]
        temp0[y+temp0-]
    """
)

Sub = inplace_to_stable(SubInplace)

def HalfAdderInplace(circuit, out, carry_out, inp):
    AddInplace(circuit, out, inp)
    Lt(circuit, carry_out, out, inp)

def FullAdder(circuit, out, carry_out, a, b, carry_in):
    temp = circuit.alloc(1)
    Add(circuit, out, a, b)
    AddInplace(circuit, out, carry_in)
    with IfNotZero(circuit, carry_in):
        Lte(circuit, carry_out, out, a)
    with IfZero(circuit, carry_in):
        Lt(circuit, carry_out, out, a)
    temp.free()

def Mul(circuit, hi, lo, a, b):
    temp = circuit.alloc(1)
    carry = circuit.alloc(1)
    hi.clear()
    lo.clear()
    Copy(circuit, a, temp)
    circuit.goto(temp)
    circuit.emit("[-")
    HalfAdderInplace(circuit, lo, carry, b)
    AddInplace(circuit, hi, carry)
    circuit.goto(temp)
    circuit.emit("]")
    temp.free()
    carry.free()


def Add32(circuit, out, a, b):
    carry_in = circuit.alloc(1)
    carry_out = circuit.alloc(1)
    carry_in.clear()
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_out, carry_in)
    carry_in.free()
    carry_out.free()


def Inc(circuit, a):
    circuit.goto(a)
    circuit.emit('+')

def Dec(circuit, a):
    circuit.goto(a)
    circuit.emit('-')

DivInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 1), ("temp2", 1), ("temp3", 1)],
    """
        temp0[-]
        temp1[-]
        temp2[-]
        temp3[-]
        x[temp0+x-]
        temp0[
         y[temp1+temp2+y-]
         temp2[y+temp2-]
         temp1[
          temp2+
          temp0-[temp2[-]temp3+temp0-]
          temp3[temp0+temp3-]
          temp2[
           temp1-
           [x-temp1[-]]+
          temp2-]
         temp1-]
         x+
        temp0]
    """)

Div = inplace_to_stable(DivInplace)

def DivMod(circuit, q, r, x, y):
    temp = circuit.alloc(1)
    Div(circuit, q, x, y)
    Copy(circuit, q, temp)
    Copy(circuit, x, r)
    circuit.goto(temp)
    circuit.emit("[-")
    SubInplace(circuit, r, y)
    circuit.goto(temp)
    circuit.emit("]")
    temp.free()
