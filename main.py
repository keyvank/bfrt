#!/usr/bin/python3
from pybrainfuck.circuit import Circuit
from pybrainfuck.io import *
from pybrainfuck.common import *
from pybrainfuck.bitwise import *
from pybrainfuck.loop import *
from pybrainfuck.math import *

if __name__ == '__main__':
    circ = Circuit()
    a = circ.new_cell()
    Put(circ, a, 123)

    PrintString(circ, "Hello World!\n==========\n")

    cnt = circ.new_cell()
    cnt2 = circ.new_cell()
    sum = circ.new_cell()
    with For(circ, cnt2, 5):
        with For(circ, cnt, 5):
            Add(circ, cnt, cnt2, sum)
            Print(circ, cnt)
            PrintString(circ, " + ")
            Print(circ, cnt2)
            PrintString(circ, " = ")
            Print(circ, sum)
            PrintString(circ, "\n")
    print(circ.compile())
