from ..bit8.common import Put, Copy

def Put32(circuit, cell_inp, val):
    for i in range(4):
        Put(circuit, cell_inp[i], val % 256)
        val = val // 256

def Copy32(circuit, cell_src, cell_dst):
    for i in range(4):
        Copy(circuit, cell_src[i], cell_dst[i])

def Const32(circuit, val):
    cells = circuit.shared_var("CONST32", 4)
    for i in range(4):
        Put(circuit, cells[i], val % 256)
        val = val // 256
    return cells

def NewConst32(circuit, val):
    cells = circuit.new_var(4)
    for i in range(4):
        Put(circuit, cells[i], val % 256)
        val = val // 256
    return cells
