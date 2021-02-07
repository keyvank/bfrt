#!/usr/bin/python3
from pybrainfuck.circuit import Circuit
from pybrainfuck.io import *
from pybrainfuck.common import *
from pybrainfuck.bitwise import *
from pybrainfuck.loop import *
from pybrainfuck.math import *
from pybrainfuck.cmp import *

if __name__ == '__main__':
    circ = Circuit()
    a = circ.new_cell()
    b = circ.new_cell()
    Put(circ, a, 123)
    Put(circ, b, 123)

    with IfNotZero(circ, a):
        PrintString(circ, "Not zero!\n")

    c = CopyOf(circ, a)
    d = CopyOf(circ, a)
    e = CopyOf(circ, a)
    Eq(circ, c, b)
    Lt(circ, d, b)
    Lte(circ, e, b)
    Print(circ, c)
    Print(circ, d)
    Print(circ, e)

    PrintString(circ, "\nHello World!\n==========\n")

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

    alt = circ.new_cell()
    with For(circ, cnt, 80):
        Not(circ, alt)
        Print(circ, alt)
    PrintString(circ, "\n")

    cond = circ.new_cell()
    cnt = circ.new_cell()
    Put(circ, cnt, 10)
    Copy(circ, cnt, cond)
    Lt(circ, cond, Const(circ, 20))
    with While(circ, cond):
        Print(circ, cnt)
        Inc(circ, cnt)
        Copy(circ, cnt, cond)
        Lt(circ, cond, Const(circ, 20))
    PrintString(circ, "\n")

    print(circ.compile())
