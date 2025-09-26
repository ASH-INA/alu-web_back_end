#!/usr/bin/env python3
"""
Tasks module
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for wait_random

    Args:
        max_delay: Maximum delay in seconds

    Returns:
        asyncio.Task: Task object for wait_random
    """
    return asyncio.create_task(wait_random(max_delay))


async def test(max_delay: int) -> float:
    """
    Test function to demonstrate task usage
    """
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)
    return task.result()


if __name__ == "__main__":
    """
    Main function to test the task_wait_random function
    """
    asyncio.run(test(5))
