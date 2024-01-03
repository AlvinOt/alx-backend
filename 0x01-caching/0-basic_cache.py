#!/usr/bin/env python3
"""
Basic cache module
"""

from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache class
    """

    def put(self, key: Any, item: Any) -> None:
        """ Add item to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """ Retrieve item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
