#!/usr/bin/env python3
"""Basic Annotations"""


def concat(str1: str, str2: str) -> str:
    """concat function with PEP 484 type annotations
    It concatenates two input string.

    Args:
        str1: first parameter
        str2: second parameter

    Returns:
        Value return is concatenated string
    """
    return str1 + str2
