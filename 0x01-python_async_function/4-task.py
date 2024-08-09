#!/usr/bin/env python3
"""
Module for executing task_wait_random multiple times and returning the results.
"""
import asyncio
from typing import List
from 3_tasks import task_wait_random  # Corrected import statement


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    """

    wait_times: List[float] = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )

    return sorted(wait_times)

