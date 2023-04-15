#!/usr/bin/env python3

"""This function returns a list of tuples containing
each element of the input list"""
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """Returns a list of tuples containing each element of the input list
    and its length.

    Args:
        lst (List[Any]): The list to process.

    Returns:
        List[Tuple[Any, int]]: The list of tuples containing each element
        of the input list and its length.
    """
    return [(i, len(i)) for i in lst]
