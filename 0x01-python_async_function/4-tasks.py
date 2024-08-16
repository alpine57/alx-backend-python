#!/usr/bin/env python3
"""Task 4"""
import asyncio
from typing import List
from task_wait_random import task_wait_random  # Importing task_wait_random from Task 3

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns a sorted list of wait times"""
    wait_times = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for _ in range(n))
    )
    return sorted(wait_times)

