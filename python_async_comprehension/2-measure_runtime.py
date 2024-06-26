#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension
    executed 4 times in parallel"""

    start = time.time()
    all = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*all)
    end = time.time()
    return end - start
