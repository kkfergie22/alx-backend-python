#!/usr/bin/env python3
""" Measure runtime."""
import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """  Measures the total execution time for `wait_n(n, max_delay)`,
    and returns the total_time / n."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
