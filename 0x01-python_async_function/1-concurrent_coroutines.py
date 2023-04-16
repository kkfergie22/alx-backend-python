#!/usr/bin/env python3
"""
This module implements the asynchronous routine wait_n that uses wait_random
"""

from typing import List
from asyncio import gather
from random import uniform

from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and
    returns the list of all the delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    unsorted_delays = await gather(*delays)
    return sorted(unsorted_delays)
