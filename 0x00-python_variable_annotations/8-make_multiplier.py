#!/usr/bin/env python3

"""This module contains a function that returns a function
which multiplies a float by a multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> callable:
    """This function returns a function that multiplies a float by a multiplier

    Args:
        multiplier (float): the multiplier

    Returns:
        callable: a function that multiplies a float by a multiplier
    """
    def multiply_by_multiplier(n: float) -> float:
        """This function multiplies a float by a multiplier

        Args:
            n (float): the float to multiply

        Returns:
            float: the product of n and multiplier
        """
        return n * multiplier
    return multiply_by_multiplier
