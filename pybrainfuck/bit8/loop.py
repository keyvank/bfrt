from .common import Put, Copy, NewConst, Clear
from .cmp import EqInplace
from .math import Inc
from .blocks import IfZero, IfNotZero

class For:
    def __init__(self, circuit, var, times):
        self.circuit = circuit
        self.times = NewConst(circuit, times)
        self.var = var

    def __enter__(self):
        Clear(self.circuit, self.var)
        self.circuit.goto(self.times)
        self.circuit.emit('[-')

    def __exit__(self, type, value, traceback):
        Inc(self.circuit, self.var)
        self.circuit.goto(self.times)
        self.circuit.emit(']')


class While:
    def __init__(self, circuit, var):
        self.circuit = circuit
        self.var = var

    def __enter__(self):
        self.circuit.goto(self.var)
        self.circuit.emit('[')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.var)
        self.circuit.emit(']')
