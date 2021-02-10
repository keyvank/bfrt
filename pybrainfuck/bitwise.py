from .common import Copy, Clear
from .helper import create_func, inplace_to_stable


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


NotInplace = create_func(
    ["x"], [("temp0", 1)],
    """
        temp0[-]
        x[temp0+x[-]]+
        temp0[x-temp0-]
    """)

Not = inplace_to_stable(NotInplace)

AndInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 1)],
    """
        temp0[-]
        temp1[-]
        x[temp1+x-]
        temp1[
         temp1[-]
         y[temp1+temp0+y-]
         temp0[y+temp0-]
         temp1[x+temp1[-]]
        ]
    """)

And = inplace_to_stable(AndInplace)

OrInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 1)],
    """
        temp0[-]
        temp1[-]
        x[temp1+x-]
        temp1[x-temp1[-]]
        y[temp1+temp0+y-]temp0[y+temp0-]
        temp1[x[-]-temp1[-]]
        x[temp1+x-]
        temp1[x+temp1[-]]
    """)

Or = inplace_to_stable(OrInplace)
