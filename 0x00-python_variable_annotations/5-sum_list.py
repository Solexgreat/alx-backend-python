#!/usr/bin/env python3
""" Return the sum of float in a list """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function sum the float in a List and return toatal """
    sum: float = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return (sum)
