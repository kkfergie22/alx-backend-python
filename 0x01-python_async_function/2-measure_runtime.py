#!/usr/bin/env python3
""" Measure runtime."""
import time
from concurrent_coroutines import wait_n as wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """  Measures the total execution time for `wait_n(n, max_delay)`,
    and returns the elapsed time."""
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    return total_time / n
