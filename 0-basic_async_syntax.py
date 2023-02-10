import random
import asyncio

async def wait_random(max_delay: int = 10 )-> float:
    ranNum = random.randint(0, max_delay)
    await asyncio.sleep(ranNum)
    return(ranNum)