#!/usr/bin/env python3
"""
This module provides a function for concatenating two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The first string to concatenate
        str2 (str): The second string to concatenate

    Returns:
        str: The concatenated string of str1 and str2
    """
    return str1 + str2


if __name__ == "__main__":
    result1 = concat("Hello", "World")
    result2 = concat("Python", "3.7")
    print(f"concat('Hello', 'World') = '{result1}'")
    print(f"concat('Python', '3.7') = '{result2}'")
    print(f"Type: {type(result1)}")
    