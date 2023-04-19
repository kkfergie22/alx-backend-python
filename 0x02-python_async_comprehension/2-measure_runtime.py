#!/usr/bin/env python3
"""Measuring the runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of four calls to async_comprehension
    running in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = time.perf_counter() - start_time
    return total_time
