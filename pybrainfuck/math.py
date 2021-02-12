from .common import *
from .helper import create_func, inplace_to_stable

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

def Inc(circuit, a):
    circuit.goto(a)
    circuit.emit('+')

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
    temp = circuit.shared_var("DIV_MOD", 1)
    Div(circuit, q, x, y)
    Copy(circuit, q, temp)
    Copy(circuit, x, r)
    circuit.goto(temp)
    circuit.emit("[-")
    SubInplace(circuit, r, y)
    circuit.goto(temp)
    circuit.emit("]")
