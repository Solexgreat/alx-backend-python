#!/usr/bin/env python3

from typing  import Sequence, Tuple, Iterator, List

def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
