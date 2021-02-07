from .common import *

def Add(circuit, a, b, c):
    temp = circuit.shared_cell("ADD")
    Copy(circuit, a, temp)
    Copy(circuit, b, c)
    circuit.goto(temp)
    circuit.emit("[-")
    circuit.goto(c)
    circuit.emit("+")
    circuit.goto(temp)
    circuit.emit("]")
