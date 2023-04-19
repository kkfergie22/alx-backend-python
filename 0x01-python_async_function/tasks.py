#!/usr/bin/env python3

""" This module creates an asyncio.Task object from wait_random """
import asyncio
from typing import List
from random import uniform
from time import sleep
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.Task object that will execute wait_random
      with the specified max_delay
    """
    return asyncio.create_task(wait_random(max_delay))
