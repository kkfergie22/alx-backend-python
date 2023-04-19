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
    new_tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*new_tasks)
    total_time = time.perf_counter() - start_time
    return total_time
