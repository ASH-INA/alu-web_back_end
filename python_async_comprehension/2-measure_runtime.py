#!/usr/bin/env python3
"""
Measure Runtime Module

This module measures the total runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time


# Import async_comprehension from the previous file



async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in 
    parallel and measure total runtime.

    Returns:
        float: Total runtime in seconds
    """
    start_time = time.time()

    # Execute four async_comprehension calls in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension

# For testing the module directly
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(runtime)

    asyncio.run(main())
