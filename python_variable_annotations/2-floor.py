#!/usr/bin/env python3
"""
This module provides a function for calculating the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to calculate the floor of

    Returns:
        int: The floor of the input number
    """
    return math.floor(n)


if __name__ == "__main__":
    test_values = [3.14, 1.11, 2.22, -1.5, 5.0]
    for value in test_values:
        result = floor(value)
        print(f"floor({value}) = {result} (type: {type(result)})")
        