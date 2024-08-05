#!/usr/bin/env python3
"""Task 4"""
import asyncio
from typing import List
from task_wait_random import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times"""
    wait_times = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for _ in range(n))
    )
    return sorted(wait_times)
