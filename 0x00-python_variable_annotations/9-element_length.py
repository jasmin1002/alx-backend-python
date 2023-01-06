#!/usr/bin/env python3
"""Basic Annotations"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length function with type annotations
    It computes each and every element's length

    Args:
        k: Stores Collection and/or Sequence

    Returns:
        return computed length
    """
    return [(i, len(i)) for i in lst]
