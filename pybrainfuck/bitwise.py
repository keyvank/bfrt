from .common import Copy, Clear
from .helper import create_func


def FirstBit(circuit, cell_inp, cell_result):
    cells = circuit.new_cells(3)
    Copy(circuit, cell_inp, cells[1])
    circuit.goto(cells[0])
    circuit.emit("+++[->[->++<]>[-<++>]<<]>[->++<]>[<<+>>[-]]<<")
    Copy(circuit, cells[0], cell_result)


def LastBit(circuit, cell_inp, cell_result):
    cells = circuit.new_cells(4)
    Copy(circuit, cell_inp, cells[1])
    circuit.goto(cells[0])
    circuit.emit("+++++++[-> [-[->>+<]>[<]<] >>[-<<+>>]<< <]")
    Copy(circuit, cells[1], cell_result)


Not = create_func(
    ["x"],
    """
        temp0[-]
        x[temp0+x[-]]+
        temp0[x-temp0-]
    """)
