#!/usr/bin/env python3
"""function index_range which takes two integer
arguments:- (page and page_size)"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
