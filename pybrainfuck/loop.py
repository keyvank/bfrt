from .common import Put, Copy

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
        self.temp = self.circuit.new_cell()
        Copy(circuit, var, self.temp)

    def __enter__(self):
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
