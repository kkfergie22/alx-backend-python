#!/usr/bin/env python3
"""This module contains a function that returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function returns a tuple

    Args:
        k (str): the string to use as key
        v (Union[int, float]): the value to use as value

    Returns:
        tuple[str, float]: the tuple
    """
    return (k, v**2)
