#!/usr/bin/env python3
"""This module contains a function that returns the sum of a list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function returns the sum of a list of floats

    Args:
        input_list (list[float]): the list of floats to sum

    Returns:
        float: the sum of the list of floats
    """
    return sum(input_list)
