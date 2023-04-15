#!/usr/bin/env python3
"""This module contains a function that returns the sum of
a mixed list of numbers"""
from typing import List


def summ_mixed_list(mxd_lst: List[int | float]) -> float:
    """This function returns the sum of a mixed list of numbers

    Args:
        mxd_lst (list[mixed]): the mixed list of numbers to sum

    Returns:
        float: the sum of the mixed list of numbers
    """
    return sum(mxd_lst)
