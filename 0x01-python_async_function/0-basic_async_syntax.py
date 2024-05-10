#!/usr/bin/env python3
'''defines async coroutine'''


import asyncio
import random


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    '''async function'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
