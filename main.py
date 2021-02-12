#!/usr/bin/python3
from pybrainfuck.circuit import Circuit
import pybrainfuck.bit8.io as b8io
import pybrainfuck.bit8.common as b8cmn
import pybrainfuck.bit8.bitwise as b8bw
import pybrainfuck.bit8.loop as b8loop
import pybrainfuck.bit8.math as b8math
import pybrainfuck.bit8.cmp as b8cmp
import pybrainfuck.bit32.math as b32math
import pybrainfuck.bit32.io as b32io
import pybrainfuck.bit32.loop as b32loop

WIDTH = 1280
HEIGHT = 800

if __name__ == '__main__':
    circ = Circuit()

    b8io.PrintString(circ, "P6 {} {} 255 ".format(WIDTH, HEIGHT))

    x = circ.new_var(4)
    y = circ.new_var(4)

    with b32loop.For32(circ, y, HEIGHT):
        with b32loop.For32(circ, x, WIDTH):
            b8io.PrintByte(circ, x[0])
            b8io.PrintByte(circ, y[0])
            b8io.PrintByte(circ, y[1])

    print(circ.compile())
