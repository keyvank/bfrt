from .common import Put32, Const32
from .cmp import Eq32
from .math import Dec32
from ..bit8.bitwise import NotInplace

class For32:
    def __init__(self, circuit, var, times):
        self.circuit = circuit
        self.times = times
        self.var = var
        self.cond = self.circuit.new_var(1)

    def __enter__(self):
        Put32(self.circuit, self.var, self.times)

        Eq32(self.circuit, self.cond, self.var, Const32(self.circuit, 0))
        NotInplace(self.circuit, self.cond)
        self.circuit.goto(self.cond)

        self.circuit.emit('[')
        Dec32(self.circuit, self.var)

    def __exit__(self, type, value, traceback):
        Eq32(self.circuit, self.cond, self.var, Const32(self.circuit, 0))
        NotInplace(self.circuit, self.cond)
        self.circuit.goto(self.cond)

        self.circuit.emit(']')
