from .common import Put

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