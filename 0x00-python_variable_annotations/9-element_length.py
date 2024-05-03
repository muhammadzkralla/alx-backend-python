#!/usr/bin/env python3
'''Element Length'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list'''
    return [(i, len(i)) for i in lst]