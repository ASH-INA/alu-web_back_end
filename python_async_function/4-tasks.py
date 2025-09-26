#!/usr/bin/env python3
"""
Tasks with wait_n module
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay
    
    Args:
        n: Number of times to spawn task_wait_random
        max_delay: Maximum delay in seconds
    
    Returns:
        List[float]: List of all delays in ascending order
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays


if __name__ == "__main__":
    """
    Main function to test the task_wait_n coroutine
    """
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
