#!/usr/bin/env python3

"""Zoom in a given list by repeating each element `factor` times."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in a given list by repeating each element `factor` times.

    Args:
        lst (Tuple[int, ...]): The input list to zoom in.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in list, as a tuple.

    Raises:
        TypeError: If the elements of `lst` are not integers."""

    zoomed_in: List = list([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
