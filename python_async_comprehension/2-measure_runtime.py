#!/usr/bin/env python3
"""
Module for measuring runtime of parallel async comprehensions
"""

import asyncio
import time
from typing import List

# Correct import - import the coroutine directly
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension four times in parallel

    Returns:
        float: Total runtime in seconds
    """
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time


# Add this to make the file executable and testable directly
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime:.2f} seconds")

    asyncio.run(main())
