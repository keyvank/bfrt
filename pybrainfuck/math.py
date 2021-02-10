from .common import *

def Add(circuit, a, b, c):
    temp = circuit.shared_var("ADD", 1)
    Copy(circuit, a, temp)
    Copy(circuit, b, c)
    circuit.goto(temp)
    circuit.emit("[-")
    circuit.goto(c)
    circuit.emit("+")
    circuit.goto(temp)
    circuit.emit("]")

def Inc(circuit, a):
    circuit.goto(a)
    circuit.emit('+')
