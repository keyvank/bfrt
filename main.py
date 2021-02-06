#!/usr/bin/python3
from pybrainfuck.circuit import Circuit
from pybrainfuck.io import *
from pybrainfuck.common import *
from pybrainfuck.bitwise import *
from pybrainfuck.loop import *

if __name__ == '__main__':
    circ = Circuit()
    a = circ.new_cell()
    Put(circ, a, 123)

    cnt = circ.new_cell()
    cnt2 = circ.new_cell()
    with For(circ, cnt2, 100):
        with For(circ, cnt, 100):
            Print(circ, cnt)
    print(circ.compile())
