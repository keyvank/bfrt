from .common import Copy, Put, Const, NewConst
from .math import DivMod, AddInplace
from .loop import Conditional
from .cmp import Lt

def Print(circuit, cell):
    cells = circuit.shared_var("PRINT", 10)
    Copy(circuit, cell, cells[0])
    circuit.goto(cells[0])
    circuit.emit('>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-\
                  <+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++\
                  <]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<')

def PrintHex(circuit, cell):
    left = circuit.shared_var("PRINT_HEX_LEFT", 1)
    right = circuit.shared_var("PRINT_HEX_RIGHT", 1)
    offset = circuit.shared_var("PRINT_HEX_OFFSET", 1)
    temp = circuit.shared_var("PRINT_HEX_TEMP", 1)
    DivMod(circuit, left, right, cell, NewConst(circuit, 16))

    Lt(circuit, temp, left, Const(circuit, 10))
    Conditional(circuit, offset, temp, NewConst(circuit, 48), NewConst(circuit, 55))
    AddInplace(circuit, left, offset)

    Lt(circuit, temp, right, Const(circuit, 10))
    Conditional(circuit, offset, temp, NewConst(circuit, 48), NewConst(circuit, 55))
    AddInplace(circuit, right, offset)

    circuit.goto(left)
    circuit.emit('.')
    circuit.goto(right)
    circuit.emit('.')

def PrintHex32(circuit, val):
    for i in range(4):
        PrintHex(circuit, val[3 - i])

def PrintString(circuit, s):
    cell = circuit.shared_var("PRINTSTRING", 1)
    for ch in s:
        Put(circuit, cell, ord(ch))
        circuit.emit('.')

def PrintByte(circuit, b):
    cell = circuit.shared_var("PRINTBYTE", 1)
    circuit.goto(b)
    circuit.emit('.')

def PrintBytes(circuit, s):
    cell = circuit.shared_var("PRINTBYTES", 1)
    for ch in s:
        Put(circuit, cell, int(ch))
        circuit.goto(cell)
        circuit.emit('.')
