from ..common import *
from ..helper import create_func, inplace_to_stable
from ..bit8.loop import IfZero, IfNotZero
from ..bit8.cmp import Lt, Lte
from ..bit8.math import FullAdder

def Add32(circuit, out, a, b):
    carry_in = circuit.shared_var("ADD32_CARRY_IN", 1)
    carry_out = circuit.shared_var("ADD32_CARRY_OUT", 1)
    Clear(circuit, carry_in)
    for i in range(4):
        FullAdder(circuit, out[i], carry_out, a[i], b[i], carry_in)
        Copy(circuit, carry_out, carry_in)
