#!/usr/bin/env python3
"""
Basic asynchronous coroutine module
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_dela

    Args:
        max_delay: Maximum delay in seconds (default 10)

    Returns:
        float: The random delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    """
    Main function to test the wait_random coroutine
    """
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
