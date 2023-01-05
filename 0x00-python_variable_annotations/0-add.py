#!/usr/bin/env python3
"""Basic Annotations"""

def add(a: float, b: float) -> float:
    """add function with PEP 484 type annotations
    It sums two decimal numbers.

    Args:
        a: first parameter
        b: second parameter

    Returns:
        Value return is decimal number
    """
    return a + b
    