#!/usr/bin/env python3
"""Basic Annotations"""
from typing import List


def sum_list(list: List[float]) -> float:
    """sum_list function with type annotations
    It calculates the sum of all entries in list

    Args:
        list: Stores collection float entry

    Returns:
        return sum of list entries
    """
    sum: float = 0.0
    for entry in list:
        sum += entry
    return sum
