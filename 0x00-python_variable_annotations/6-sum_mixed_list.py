#!/usr/bin/env python3
"""   """

from typing import Union, List


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """   """
    sum: float = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return (sum)
