#!/usr/bin/env python3
"""
This module provides a function for summing a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all floating-point numbers in a list.

    Args:
        input_list (List[float]): A list of floating-point numbers to be summed

    Returns:
        float: The sum of all numbers in the input list
    """
    return sum(input_list)

# function call
if __name__ == "__main__":
    floats = [3.14, 1.11, 2.22]
    result = sum_list(floats)
    
    print(f"sum_list({floats}) = {result}")
    print(f"Matches built-in sum(): {result == sum(floats)}")
    print(f"Type: {type(result)}")
    print(f"Function annotations: {sum_list.__annotations__}")