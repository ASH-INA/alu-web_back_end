#!/usr/bin/env python3
"""
Concurrent coroutines module
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    
    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay in seconds
    
    Returns:
        List[float]: List of all delays in ascending order
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays


if __name__ == "__main__":
    """
    Main function to test the wait_n coroutine
    """
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
