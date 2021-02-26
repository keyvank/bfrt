from ..bit8.cmp import Eq
from ..bit8.bitwise import AndInplace
from ..bit8.common import Put

def Eq32(circuit, res, x, y):
    temp = circuit.alloc(1)
    Put(circuit, res, 1)
    for i in range(4):
        Eq(circuit, temp, x[i], y[i])
        AndInplace(circuit, res, temp)
    temp.free()
