#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('Task-2').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))