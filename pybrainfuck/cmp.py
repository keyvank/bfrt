from .common import Copy
from .helper import create_func


# Brainfuck Algorithms
# x = x == y
Eq = create_func(
    ["x", "y"], ["temp0", "temp1"],
    """
        temp0[-]
        temp1[-]
        x[temp1+x-]+
        y[temp1-temp0+y-]
        temp0[y+temp0-]
        temp1[x-temp1[-]]
    """)

# Brainfuck Algorithms
# x = x < y
Lt = create_func(
    ["x", "y"], ["temp0", "temp1"],
    """
        temp0[-]
        temp1[-] >[-]+ >[-] <<
        y[temp0+ temp1+ y-]
        temp0[y+ temp0-]
        x[temp0+ x-]+
        temp1[>-]> [< x- temp0[-] temp1>->]<+<
        temp0[temp1- [>-]> [< x- temp0[-]+ temp1>->]<+< temp0-]
    """)

# Brainfuck Algorithms
# x = x <= y
Lte = create_func(
    ["x", "y"], ["temp0", "temp1"],
    """
        temp0[-]
        temp1[-] >[-]+ >[-] <<
        y[temp0+ temp1+ y-]
        temp1[y+ temp1-]
        x[temp1+ x-]
        temp1[>-]> [< x+ temp0[-] temp1>->]<+<
        temp0[temp1- [>-]> [< x+ temp0[-]+ temp1>->]<+< temp0-]
    """)
