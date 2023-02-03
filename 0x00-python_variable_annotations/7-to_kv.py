#!/usr/bin/env python3
"""  """

from typing import Tuple, Union

def to_kv(k:str, v: Union[int, float]) -> Tuple:
    """   """
    tup: Tuple[str, float] = [k, v*v]
    return (tup)
