from ..bit8 import Put

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256
