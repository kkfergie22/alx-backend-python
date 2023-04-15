#!/usr/bin/env python3

"""This function returns a list of tuples containing
each element of the input list"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing each element of the input list
    and its length.

    Args:
      The list to process.

    Returns:
      The list of tuples containing each element
        of the input list and its length.
    """
    return [(i, len(i)) for i in lst]
