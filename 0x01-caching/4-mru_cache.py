#!/usr/bin/env python3
"""MRU Caching system demonstration"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A class for LRU caching system

    Args:
        BaseCaching (Base Class for caching):
        parent class template for caching
    """
    def __init__(self):
        """Constructor initialization
        """
        super().__init__()

    def put(self, key, item):
        """Updates the cache with the given key and item.

        Args:
            key (str): The key to add to the cache.
            item (any): The item to add to the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the Most Recently Used item and remove it
                # Get the last key (most recent)
                mru_key = next(reversed(self.cache_data))
                print("DISCARD: {}".format(mru_key))  # Print key discarded
                del self.cache_data[mru_key]  # Rm the most recently used item
            self.cache_data[key] = item  # Add or update the item in the cache

    def get(self, key):
        """Returns an item from the cache based on the specified key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The item associated with the key,
            or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            item = self.cache_data[key]
            # No need to adjust order in MRU,
            # as get operation already makes it most recent
            return item
        return None
