#!/usr/bin/env python3
""" Return a Tuple and Sequence of int """

from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function tha Iterate through the sequence """
    return ([(i, len(i)) for i in lst])
