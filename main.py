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
    a = circ.new_var(1)
    b = circ.new_var(1)
    c = circ.new_var(1)
    d = circ.new_var(1)
    e = circ.new_var(1)
    f = circ.new_var(1)
    g = circ.new_var(1)
    Put(circ, a, 100)
    Put(circ, b, 42)
    Print(circ, a)
    PrintString(circ, "-")
    Print(circ, b)

    Eq(circ, c, a, b)
    Lt(circ, d, a, b)
    Lte(circ, e, a, b)
    DivMod(circ, f, g, a, b)

    PrintString(circ, "\n-----\n")
    PrintString(circ, "Eq: ")
    Print(circ, c)
    PrintString(circ, "\nLt: ")
    Print(circ, d)
    PrintString(circ, "\nLte: ")
    Print(circ, e)
    PrintString(circ, "\nDiv: ")
    Print(circ, f)
    PrintString(circ, "\nMod: ")
    Print(circ, g)
    PrintString(circ, "\n")

    with IfNotZero(circ, a):
        PrintString(circ, "a is not zero!\n")

    Put(circ, a, 0)
    Put(circ, b, 1)
    Print(circ, a)
    PrintString(circ, "-")
    Print(circ, b)

    And(circ, c, a, b)
    Or(circ, d, a, b)
    Not(circ, e, a)
    PrintString(circ, "\n-----\n")
    PrintString(circ, "And: ")
    Print(circ, c)
    PrintString(circ, "\nOr: ")
    Print(circ, d)
    PrintString(circ, "\nNot: ")
    Print(circ, e)
    PrintString(circ, "\n")

    PrintString(circ, "\nHello World!\n==========\n")

    cnt = circ.new_var(1)
    cnt2 = circ.new_var(1)
    sum = circ.new_var(1)
    with For(circ, cnt2, 5):
        with For(circ, cnt, 5):
            Add(circ, sum, cnt, cnt2)
            Print(circ, cnt)
            PrintString(circ, " + ")
            Print(circ, cnt2)
            PrintString(circ, " = ")
            Print(circ, sum)
            PrintString(circ, "\n")

    alt = circ.new_var(1)
    with For(circ, cnt, 80):
        Not(circ, alt, alt)
        Print(circ, alt)
    PrintString(circ, "\n")

    cond = circ.new_var(1)
    cnt = circ.new_var(1)
    Put(circ, cnt, 10)
    Lt(circ, cond, cnt, Const(circ, 20))
    with While(circ, cond):
        Print(circ, cnt)
        Inc(circ, cnt)
        Lt(circ, cond, cnt, Const(circ, 20))
    PrintString(circ, "\n")

    print(circ.compile())
