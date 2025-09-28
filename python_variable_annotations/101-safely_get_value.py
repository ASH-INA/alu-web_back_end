#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a mapping.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a mapping by key,returning
    default if key not found.

    Args:
        dct (Mapping): A mapping (dict-like) object
        key (Any): The key to look up in the mapping
        default (Union[T, None]): The default value to return if key not found

    Returns:
        Union[Any, T]: The value associated with the key or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    # Demonstration
    test_dict = {"a": 1, "b": 2, "c": 3}

    result1 = safely_get_value(test_dict, "a", "default")
    result2 = safely_get_value(test_dict, "x", "default")
    result3 = safely_get_value(test_dict, "b", 100)

    print(f"safely_get_value({test_dict}, 'a', 'default') = {result1}")
    print(f"safely_get_value({test_dict}, 'x', 'default') = {result2}")
    print(f"safely_get_value({test_dict}, 'b', 100) = {result3}")
    print(f"Function annotations: {safely_get_value.__annotations__}")
