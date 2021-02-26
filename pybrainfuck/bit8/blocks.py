from .common import Copy
from .cmp import EqInplace

class IfNotZero:
    def __init__(self, circuit, var):
        self.circuit = circuit
        self.temp = self.circuit.alloc(1)
        Copy(circuit, var, self.temp)

    def __enter__(self):
        self.circuit.goto(self.temp)
        self.circuit.emit('[')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.temp)
        self.circuit.emit('[-]]')
        self.temp.free()

class IfZero:
    def __init__(self, circuit, var):
        self.circuit = circuit
        self.temp = self.circuit.alloc(1)
        self.zero = self.circuit.alloc_const8(0)
        Copy(circuit, var, self.temp)

    def __enter__(self):
        EqInplace(self.circuit, self.temp, self.zero)
        self.circuit.goto(self.temp)
        self.circuit.emit('[')

    def __exit__(self, type, value, traceback):
        self.circuit.goto(self.temp)
        self.circuit.emit('[-]]')
        self.temp.free()
        self.zero.free()

# out = cond ? x : y
def Conditional(circuit, out, cond, x, y):
    with IfNotZero(circuit, cond):
        Copy(circuit, x, out)
    with IfZero(circuit, cond):
        Copy(circuit, y, out)
