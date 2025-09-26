#!/usr/bin/env python3
"""
This module provides a function that returns a tuple containing a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a number.

    Args:
        k (str): The string to be included as the first element of the tuple
        v (Union[int, float]): The integer or float to be squared

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k, 
                          and the second element is the square of v as a float
    """
    return (k, float(v * v))


# function call
if __name__ == "__main__":
    result1 = to_kv("eggs", 3)
    result2 = to_kv("school", 0.02)
    
    print(f"to_kv('eggs', 3) = {result1}")
    print(f"to_kv('school', 0.02) = {result2}")
    print(f"Type of result1: {type(result1)}")
    print(f"Type of result1[1]: {type(result1[1])}")
    print(f"Function annotations: {to_kv.__annotations__}")