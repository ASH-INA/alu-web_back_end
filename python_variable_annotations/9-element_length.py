#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples containing elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with sequences and their lengths
    """
    return [(i, len(i)) for i in lst]


# function call
if __name__ == "__main__":
    test_list1 = ["hello", "world", "python"]
    test_list2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    result1 = element_length(test_list1)
    result2 = element_length(test_list2)
    
    print(f"element_length({test_list1}) = {result1}")
    print(f"element_length({test_list2}) = {result2}")
    print(f"Function annotations: {element_length.__annotations__}")