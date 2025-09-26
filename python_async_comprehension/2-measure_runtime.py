#!/usr/bin/env python3
"""
Measure Runtime Module

This module contains a coroutine that measures the runtime of executing
four async comprehensions in parallel.
"""

import asyncio
import time
from typing import List

# Import the async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing four async comprehensions in parallel.

    This coroutine executes async_comprehension four times in parallel using
    asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.

    Explanation:
        The total runtime is roughly 10 seconds because even though the four
        async comprehensions run in parallel, each async_comprehension takes
        about 10 seconds to complete (due to the 1-second wait in the generator
        repeated 10 times). Since they run concurrently, they complete in
        approximately the same time as a single execution.
    """
    start_time = time.time()

    # Execute four async comprehensions in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time

# For testing the module directly
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime:.2f} seconds")

    asyncio.run(main())
