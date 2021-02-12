#!/usr/bin/python3
from pybrainfuck.circuit import Circuit
from pybrainfuck.bit8.io import *
from pybrainfuck.bit8.common import *
from pybrainfuck.bit8.bitwise import *
from pybrainfuck.bit8.loop import *
from pybrainfuck.bit8.math import *
from pybrainfuck.bit8.cmp import *

if __name__ == '__main__':
    circ = Circuit()

    aa = circ.new_var(4)
    Put32(circ, aa, 0xabcdefed)
    bb = circ.new_var(4)
    Put32(circ, bb, 0xbcdefedc)
    cc = circ.new_var(4)
    Add32(circ, cc, aa, bb)

    PrintHex32(circ, aa)
    PrintString(circ, "+")
    PrintHex32(circ, bb)
    PrintString(circ, "=")
    PrintHex32(circ, cc)

    PrintString(circ, "\n")

    a = circ.new_var(1)
    b = circ.new_var(1)
    c = circ.new_var(1)
    d = circ.new_var(1)
    e = circ.new_var(1)
    f = circ.new_var(1)
    g = circ.new_var(1)
    Put(circ, a, 100)

    with IfZero(circ, a):
        PrintString(circ,"Is zero!\n")

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

    PrintString(circ, "------\n")
    with For(circ, cnt, 255):
        Print(circ, cnt)
        PrintString(circ, " = 0x")
        PrintHex(circ, cnt)
        PrintString(circ, "\n")

    print(circ.compile())
