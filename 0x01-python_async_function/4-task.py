#!/usr/bin/env python3
"""
Module for executing task_wait_random multiple times and returning the results.
"""
import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times 
    """
    # Gather all the delays from task_wait_random calls
    wait_times = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )

    # Return the list of delays in ascending order
    return sorted(wait_times)


