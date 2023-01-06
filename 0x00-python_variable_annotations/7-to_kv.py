#!/usr/bin/env python3
"""Basic Annotations"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv function with type annotations
    It calculates the square of int or float number

    Args:
        k: Stores data description
        v: Stores square of number

    Returns:
        return collection of str and float number
    """
    tple: Tuple[str, float] = k, v * v
    return tple
