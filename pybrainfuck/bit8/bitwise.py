from .common import Copy
from ..helper import create_func, inplace_to_stable


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
