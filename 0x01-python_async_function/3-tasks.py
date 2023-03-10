#!/usr/bin/env python3
"""Wait random"""

import asyncio

wait_random = __import__('task-2').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes a integer `max_delay` and returns an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
