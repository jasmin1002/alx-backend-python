#!/usr/bin/env python3
import math
"""Basic Annotations"""


def floor(n: float) -> float:
    """floor function with PEP 484 type annotations
    It rounds input number to the nearest whole no.

    Args:
        n: number to round off

    Returns:
        Value return is decimal number
    """
    return math.floor(n)
