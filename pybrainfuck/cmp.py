from .common import Copy
from .helper import create_func, inplace_to_stable


# Brainfuck Algorithms
# x = x == y
EqInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 1)],
    """
        temp0[-]
        temp1[-]
        x[temp1+x-]+
        y[temp1-temp0+y-]
        temp0[y+temp0-]
        temp1[x-temp1[-]]
    """)

Eq = inplace_to_stable(EqInplace)

# Brainfuck Algorithms
# x = x < y
LtInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 3)],
    """
        temp0[-]
        temp1[-] >[-]+ >[-] <<
        y[temp0+ temp1+ y-]
        temp0[y+ temp0-]
        x[temp0+ x-]+
        temp1[>-]> [< x- temp0[-] temp1>->]<+<
        temp0[temp1- [>-]> [< x- temp0[-]+ temp1>->]<+< temp0-]
    """)

Lt = inplace_to_stable(LtInplace)

# Brainfuck Algorithms
# x = x <= y
LteInplace = create_func(
    ["x", "y"], [("temp0", 1), ("temp1", 3)],
    """
        temp0[-]
        temp1[-] >[-]+ >[-] <<
        y[temp0+ temp1+ y-]
        temp1[y+ temp1-]
        x[temp1+ x-]
        temp1[>-]> [< x+ temp0[-] temp1>->]<+<
        temp0[temp1- [>-]> [< x+ temp0[-]+ temp1>->]<+< temp0-]
    """)

Lte = inplace_to_stable(LteInplace)
