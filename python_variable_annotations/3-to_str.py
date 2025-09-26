#!/usr/bin/env python3
"""
This module provides a function for converting a float to a string.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to its string representation.

    Args:
        n (float): The floating-point number to convert to string

    Returns:
        str: The string representation of the input number
    """
    return str(n)


if __name__ == "__main__":
    test_values = [3.14, 2.0, -1.5, 0.0, 100.25]
    for value in test_values:
        result = to_str(value)
        print(f"to_str({value}) = '{result}' (type: {type(result)})")
        