#!/usr/bin/env python3
""" Return tuple  """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function takes teo aurgment str and float/int and return the
    tuple of the str and square of the float"""
    return (k, v**2)
