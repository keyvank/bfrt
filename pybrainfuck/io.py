from .common import Copy, Put


def Print(circuit, cell):
    cells = circuit.shared_var("PRINT", 9)
    Copy(circuit, cell, cells[0])
    circuit.goto(cells[0])
    circuit.emit('>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-\
                  <+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++\
                  <]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<')

def PrintString(circuit, s):
    cell = circuit.shared_var("PRINTSTRING", 1)
    for ch in s:
        Put(circuit, cell, ord(ch))
        circuit.emit('.')
