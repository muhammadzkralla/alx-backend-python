#!/usr/bin/env python3
""" Run async function """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return float value after random delay
    """

    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val