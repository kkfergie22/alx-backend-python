from typing import Any, Dict, TypeVar

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: V = None) -> V:
    """Returns the value associated with the given key in a dictionary, or
    a default value if the key is not present in the dictionary.

    Args:
        dct (Dict[K, V]): The dictionary to search.
        key (K): The key to look up.
        default (V, optional): The value to return if the key is not present.
            Defaults to None.

    Returns:
        V: The value associated with the key in the dictionary,
        or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
