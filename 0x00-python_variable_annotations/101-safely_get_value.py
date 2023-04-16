#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union

K = TypeVar('K')
V = TypeVar('V')
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Safely gets a value from a dictionary.

    Args:
        dct: A mapping containing the key-value pairs.
        key: The key to look up in the dictionary.
        default: The default value to return
          if the key is not found. Defaults to None.

    Returns:
        The value associated with the key in the dictionary
        if the key is found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
