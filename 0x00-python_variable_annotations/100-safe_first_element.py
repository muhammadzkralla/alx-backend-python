#!/usr/bin/env python3
'''Safe Call'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element if it exists'''
    if lst:
        return lst[0]
    else:
        return None
