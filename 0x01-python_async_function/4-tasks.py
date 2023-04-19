#!/usr/bin/env python3

""" This module creates an asyncio.Task object from task_wait_random """

import asyncio
from typing import List

from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns a list of the delays (float values) in ascending order.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
