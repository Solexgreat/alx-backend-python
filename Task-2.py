import asyncio
from time import time

wait_n = __import__('Task-1').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time() - start_time
    return(total_time/n)
