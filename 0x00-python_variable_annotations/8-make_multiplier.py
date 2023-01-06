#!/usr/bin/env python3
"""Basic Annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function with type annotations
    It demonstrates closure in python

    Args:
        k: Stores number of multiplicand

    Returns:
        return callable with access to capture variable
    """
    return lambda new_mul: multiplier * new_mul
