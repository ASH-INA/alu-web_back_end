#!/usr/bin/env python3
"""
Async Comprehension Module

This module contains a coroutine that uses async comprehension to collect
random numbers from an asynchronous generator.
"""

import asyncio
from typing import List

# Import the async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension.

    This coroutine uses an async comprehension over async_generator
    to collect 10 random numbers and return them as a list.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]

# For testing the module directly
if __name__ == "__main__":
    async def main():
        result = await async_comprehension()
        print(result)

    asyncio.run(main())
