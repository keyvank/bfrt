from ..bit8.common import Put, Copy

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256

def Copy32(circuit, cell_src, cell_dst):
    for i in range(4):
        Copy(circuit, cell_src[i], cell_dst[i])
