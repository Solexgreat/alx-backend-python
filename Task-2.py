
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int )-> List[float]:
    create = [asyncio.create_task(wait_random(max_delay)) 
                        for i in range(n) ]
    completed_task = []
    for task in asyncio.as_completed(create):
        completed_task.append(await task)
    return (completed_task)   