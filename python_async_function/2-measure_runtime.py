#!/usr/bin/env python3
"""
Runtime measurement module
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    
    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay in seconds
    
    Returns:
        float: Average time per operation (total_time / n)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    """
    Main function to test the measure_time function
    """
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
