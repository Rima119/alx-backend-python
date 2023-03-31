#!/usr/bin/env python3
"""Type-annotated function that returns sum of list of
integers and floats as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum as float"""
    return sum(mxd_lst)
