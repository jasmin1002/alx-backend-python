#!/usr/bin/env python3
"""Basic Annotations"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list function with type annotations
    It calculates the sum of all entries in list

    Args:
        list: Stores collection of both int and float entry

    Returns:
        return sum of list entries
    """
    sum: float = 0.0
    for entry in mxd_lst:
        sum += entry
    return sum
