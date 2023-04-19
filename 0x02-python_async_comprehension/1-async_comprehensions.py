#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers using
    an async comprehension"""
    return [x async for x in async_generator()]
