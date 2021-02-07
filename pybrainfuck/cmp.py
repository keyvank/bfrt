from .common import Copy
from .helper import create_func

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

Gt = create_func(
    ["x", "y", "z"],
    """
        temp0[-]temp1[-]z[-]
        x[ temp0+
               y[- temp0[-] temp1+ y]
           temp0[- z+ temp0]
           temp1[- y+ temp1]
           y- x- ]
    """)
