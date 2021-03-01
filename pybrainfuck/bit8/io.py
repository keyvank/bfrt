from .common import Copy, Put
from .math import DivMod, AddInplace
from .blocks import Conditional
from .cmp import Lt

def Print(circuit, cell):
    cells = circuit.alloc(10)
    Copy(circuit, cells[0], cell)
    circuit.goto(cells[0])
    circuit.emit('>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-\
                  <+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++\
                  <]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<')
    cells.free()

def PrintHex(circuit, cell):
    left = circuit.alloc(1)
    right = circuit.alloc(1)
    offset = circuit.alloc(1)
    temp = circuit.alloc(1)

    consts = circuit.alloc(2)

    Put(circuit, consts[0], 16)
    DivMod(circuit, left, right, cell, consts[0])

    Put(circuit, consts[0], 10)
    Lt(circuit, temp, left, consts[0])
    Put(circuit, consts[0], 48)
    Put(circuit, consts[1], 55)
    Conditional(circuit, offset, temp, consts[0], consts[1])
    AddInplace(circuit, left, offset)

    Put(circuit, consts[0], 10)
    Lt(circuit, temp, right, consts[0])
    Put(circuit, consts[0], 48)
    Put(circuit, consts[1], 55)
    Conditional(circuit, offset, temp, consts[0], consts[1])
    AddInplace(circuit, right, offset)

    circuit.goto(left)
    circuit.emit('.')
    circuit.goto(right)
    circuit.emit('.')

    left.free()
    right.free()
    offset.free()
    temp.free()
    consts.free()

def PrintHex32(circuit, val):
    for i in range(4):
        PrintHex(circuit, val[3 - i])

def PrintString(circuit, s):
    cell = circuit.alloc(1)
    for ch in s:
        Put(circuit, cell, ord(ch))
        circuit.emit('.')
    cell.free()

def PrintByte(circuit, b):
    cell = circuit.alloc(1)
    circuit.goto(b)
    circuit.emit('.')
    cell.free()

def PrintBytes(circuit, s):
    cell = circuit.alloc(1)
    for ch in s:
        Put(circuit, cell, int(ch))
        circuit.goto(cell)
        circuit.emit('.')
    cell.free()
