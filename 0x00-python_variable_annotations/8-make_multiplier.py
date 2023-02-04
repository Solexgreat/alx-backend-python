#!/usr/bin/env python3
""" Return Multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Fuction that return a callback """ 
    return (lambda x: multiplier * x)
