#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of any type of elements

    Returns:
        Union[Any, None]: The first element of the sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    # Demonstration
    test_list = [1, 2, 3]
    test_tuple = ("a", "b", "c")
    test_string = "hello"
    empty_list = []

    print(f"safe_first_element({test_list}) = {safe_first_element(test_list)}")
    print(f"safe_first_element({test_tuple}) = {safe_first_element(test_tuple)}")
    print(f"safe_first_element('{test_string}') = {safe_first_element(test_string)}")
    print(f"safe_first_element({empty_list}) = {safe_first_element(empty_list)}")
    print(f"Function annotations: {safe_first_element.__annotations__}")
