#!/usr/bin/env python3
import time
from typing import List
import asyncio
from basic_async_syntax import wait_random
from concurrent_coroutines import wait_n


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of the delays (float values) in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n.
    Uses the time module to measure an approximate elapsed time.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
