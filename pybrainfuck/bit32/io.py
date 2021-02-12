from ..bit8.io import PrintHex

def PrintHex32(circuit, val):
    for i in range(4):
        PrintHex(circuit, val[3 - i])
