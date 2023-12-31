#!/usr/bin/env python3
"""
LRU Caching module
"""

from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Cache class
    """

    def __init__(self):
        """ Initializing LRU Cache """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """ Add item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key: Any) -> Any:
        """ Retrieve item from cache """
        if key is None or key not in self.cache_data:
            return None

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
