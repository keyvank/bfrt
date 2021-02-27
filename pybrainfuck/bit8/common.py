from ..helper import create_func

# Sets inp to zero
Clear = create_func(["inp"], [], "inp[-]")

# dst = src
Copy = create_func(
    ["src", "dst"], [("temp", 1)],
    """
        dst[-]
        src[-temp+dst+src]
        temp[-src+temp]
    """)

# Puts value in inp
def Put(circuit, cell_inp, val):
    Clear(circuit, cell_inp)
    circuit.goto(cell_inp)
    circuit.emit('+' * val)

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256
