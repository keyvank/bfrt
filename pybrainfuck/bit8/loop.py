from .common import Put, Copy, Const
from .cmp import EqInplace

class For:
    def __init__(self, circuit, var, times):
        self.circuit = circuit
        self.times = times
        self.var = var

    def __enter__(self):
        self.circuit.goto(self.var)
        Put(self.circuit, self.var, self.times)
        self.circuit.emit('[-')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.var)
        self.circuit.emit(']')

class IfNotZero:
    def __init__(self, circuit, var):
        self.circuit = circuit
        self.temp = self.circuit.new_var(1)
        Copy(circuit, var, self.temp)

    def __enter__(self):
        self.circuit.goto(self.temp)
        self.circuit.emit('[')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.temp)
        self.circuit.emit('[-]]')

class IfZero:
    def __init__(self, circuit, var):
        self.circuit = circuit
        self.temp = self.circuit.new_var(1)
        Copy(circuit, var, self.temp)

    def __enter__(self):
        EqInplace(self.circuit, self.temp, Const(self.circuit, 0))
        self.circuit.goto(self.temp)
        self.circuit.emit('[')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.temp)
        self.circuit.emit('[-]]')


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

# out = cond ? x : y
def Conditional(circuit, out, cond, x, y):
    with IfNotZero(circuit, cond):
        Copy(circuit, x, out)
    with IfZero(circuit, cond):
        Copy(circuit, y, out)
