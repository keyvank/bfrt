# Sets inp to zero
def Clear(circuit, cell_inp):
    circuit.goto(cell_inp)
    circuit.emit("[-]")

# Copies src to dst
def Copy(circuit, cell_src, cell_dst):
    cell_temp = circuit.alloc(1)
    Clear(circuit, cell_dst)

    # Move src to temp and dst
    circuit.goto(cell_src)
    circuit.emit('[-')
    circuit.goto(cell_temp)
    circuit.emit('+')
    circuit.goto(cell_dst)
    circuit.emit('+')
    circuit.goto(cell_src)
    circuit.emit(']')

    # Move temp to src
    circuit.goto(cell_temp)
    circuit.emit('[-')
    circuit.goto(cell_src)
    circuit.emit('+')
    circuit.goto(cell_temp)
    circuit.emit(']')

    cell_temp.free()

# Puts value in inp
def Put(circuit, cell_inp, val):
    Clear(circuit, cell_inp)
    circuit.goto(cell_inp)
    circuit.emit('+' * val)

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256
