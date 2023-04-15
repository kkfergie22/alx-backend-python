#!/usr/bin/env python3

"""This module contains a function that returns the first element of a list"""

# The types of the elements of the input are not known
from typing import Any, Optional, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Optional[Union[Any, None]]:
    """This function returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
