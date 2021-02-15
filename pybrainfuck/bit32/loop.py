from .common import Put32, NewConst32
from .cmp import Eq32
from .math import Inc32
from ..bit8.bitwise import NotInplace

class For32:
    def __init__(self, circuit, var, times):
        self.circuit = circuit
        self.times = NewConst32(self.circuit, times)
        self.var = var
        self.cond = self.circuit.new_var(1)

    def __enter__(self):
        Put32(self.circuit, self.var, 0)

        Eq32(self.circuit, self.cond, self.var, self.times)
        NotInplace(self.circuit, self.cond)
        self.circuit.goto(self.cond)

        self.circuit.emit('[')
        Inc32(self.circuit, self.var)

    def __exit__(self, type, value, traceback):
        Eq32(self.circuit, self.cond, self.var, self.times)
        NotInplace(self.circuit, self.cond)
        self.circuit.goto(self.cond)

        self.circuit.emit(']')
