from ..bit8.common import Put, Copy

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256

def Copy32(circuit, cell_dst, cell_src):
    for i in range(4):
        Copy(circuit, cell_dst[i], cell_src[i])
