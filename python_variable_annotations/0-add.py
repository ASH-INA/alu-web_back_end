#!/usr/bin/env python3
"""
This module provides a function for adding two floating-point numbers.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns their sum.

    Args:
        a (float): The first number to add
        b (float): The second number to add

    Returns:
        float: The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    result = add(1.11, 2.22)
    expected = 1.11 + 2.22
    print(f"add(1.11, 2.22) = {result}")
    print(f"1.11 + 2.22 = {expected}")
    print(f"Results match: {result == expected}")
    print(f"Type of result: {type(result)}")
    print(f"Function annotations: {add.__annotations__}")
    