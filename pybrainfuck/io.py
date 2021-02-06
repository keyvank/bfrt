from .common import Copy


def Print(circuit, cell):
    cells = circuit.shared_cells("PRINT", 9)
    Copy(circuit, cell, cells[0])
    circuit.goto(cells[0])
    circuit.emit('>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-\
                  <+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++\
                  <]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<')
