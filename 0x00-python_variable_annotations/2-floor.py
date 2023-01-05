#!/usr/bin/env python3
"""Basic Annotations"""
import math


def floor(n: float) -> int:
    """floor function with PEP 484 type annotations
    It rounds input number to the nearest whole no.

    Args:
        n: number to round off

    Returns:
        Value return is integer number
    """
    return math.floor(n)
