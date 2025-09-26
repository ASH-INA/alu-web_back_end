#!/usr/bin/env python3
"""
This module provides a function for summing a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floats

    Returns:
        float: The sum of all numbers in the input list as a float
    """
    return float(sum(mxd_lst))

# function call
if __name__ == "__main__":
    mixed = [5, 4, 3.14, 666, 0.99]
    result = sum_mixed_list(mixed)
    
    print(f"sum_mixed_list({mixed}) = {result}")
    print(f"Matches built-in sum(): {result == sum(mixed)}")
    print(f"Type: {type(result)}")
    print(f"Function annotations: {sum_mixed_list.__annotations__}")