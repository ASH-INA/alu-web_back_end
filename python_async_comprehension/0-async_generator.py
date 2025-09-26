#!/usr/bin/env python3
"""
Async Generator Module

This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Asynchronous generator that yields random numbers.

    This coroutine loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# For testing the module directly
if __name__ == "__main__":
    async def main():
        async for value in async_generator():
            print(value)

    asyncio.run(main())
