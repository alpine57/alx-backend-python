#!/usr/bin/env python
"""task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """enerates a sequence of 10digits"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
