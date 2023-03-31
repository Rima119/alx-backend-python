#!/usr/bin/env python3
"""Type-annotated function, takes str and int or float, returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns str, square of v as float"""
    return k, v**2
