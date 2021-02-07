from .common import Copy

def Eq(circuit, a, b, result):
    temp = circuit.shared_cell("EQ")
    Copy(circuit, a, result)
    Copy(circuit, b, temp)

    circuit.goto(result)
    circuit.emit("[-")
    circuit.goto(temp)
    circuit.emit("-")
    circuit.goto(result)
    circuit.emit("]+")
    circuit.goto(temp)
    circuit.emit("[")
    circuit.goto(result)
    circuit.emit("-")
    circuit.goto(temp)
    circuit.emit("[-]]")
