def func(x):
    """
    >>> func(0)
    1.0
    >>> func(1)
    5.0
    """
    return float(((x**4)+(4**x)))
import doctest
doctest.testmod()
