#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value

    Returns:
        Callable[[float], float]:A function that multiplies input by multiplier
    """

    def multiplier_function(x: float) -> float:
        """Multiplies the input by the multiplier."""
        return x * multiplier

    return multiplier_function


if __name__ == "__main__":
    fun = make_multiplier(2.22)
    result = fun(2.22)
    print(f"make_multiplier(2.22) returns a function")
    print(f"Calling the returned function with 2.22: {result}")
    print(f"Function annotations: {make_multiplier.__annotations__}")
