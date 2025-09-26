#!/usr/bin/env python3
"""
This module provides a function for zooming arrays with type checking.
"""

from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms an array by repeating each element a specified number of times.

    Args:
        lst (Tuple): The tuple to zoom
        factor (int): The zoom factor (default: 2)

    Returns:
        List: A list with each element repeated factor times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    array = (12, 72, 91)  # Changed from list to tuple

    zoom_2x = zoom_array(array)
    zoom_3x = zoom_array(array, 3)  # Changed from 3.0 to 3

    print(f"Original array: {array}")
    print(f"Zoom 2x: {zoom_2x}")
    print(f"Zoom 3x: {zoom_3x}")
    print(f"Function annotations: {zoom_array.__annotations__}")
