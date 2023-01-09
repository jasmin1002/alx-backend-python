#!/usr/bin/env python3
"""Basic asynchronous code"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """
    Async wait_random delays program within of [0 - max_delay)
    or [0 - max_delay] depending on rounding

    Args:
        max_delay: upper boundary

    Returns:
        returns amount of time in sec the program is paused.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
