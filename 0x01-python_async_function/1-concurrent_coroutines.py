#!/usr/bin/env python3
"""Basic asynchronous code"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay) -> List[float]:
    """
    Async wait_random delays program within of [0 - max_delay)
    or [0 - max_delay] depending on rounding

    Args:
        max_delay: upper boundary

    Returns:
        returns amount of time in sec the program is paused.
    """
    lst = []
    for i in range(n):
        delay = await wait_random(max_delay)
        lst.append(delay)
    return lst
