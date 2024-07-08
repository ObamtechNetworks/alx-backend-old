#!/usr/bin/env python3
"""MRU Caching system demonstration"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class for LFU (Least Frequently Used) caching system.

    Inherits from BaseCaching and implements LFU eviction strategy
    when the cache reaches its maximum capacity.

    Args:
        BaseCaching (class): Parent class template for caching.

    Attributes:
        access_frequency (dict): Keeps track of the access frequency of keys.
        access_order (list): Tracks the order of key accesses.

    Methods:
        __init__():
            Initializes the LFUCache instance.

        put(key, item):
            Adds or updates an item in the cache.
            Implements LFU eviction strategy when the cache is full.

        get(key):
            Retrieves an item from the cache based on the specified key.
            Updates the access frequency and order of the accessed key.
    """

    def __init__(self):
        """Initializes the LFUCache instance."""
        super().__init__()
        self.access_frequency = {}  # Track access frequency of keys
        self.access_order = []  # Track access order of keys

    def put(self, key, item):
        """Adds or updates an item in the cache.

        If the cache is full (reaches BaseCaching.MAX_ITEMS):
        - Discards the least frequently used item (LFU).
        - If multiple items have the same frequency, uses LRU to decide.

        Args:
            key (str): The key to add or update in the cache.
            item (any): The item to add or update in the cache.
        """
        if key is None or item is None:
            return

        # Add or update the item in the cache
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.access_frequency:
                # Find the item with the minimum access frequency
                min_frequency = min(self.access_frequency.values())
                items_with_min_frequency = [
                    k for k, v in self.access_frequency.items()
                    if v == min_frequency]

                # If there are multiple items with the same minimum frequency,
                # use LRU to decide which one to discard
                if self.access_order:
                    lru_key = None
                    for key in self.access_order:
                        if key in items_with_min_frequency:
                            lru_key = key
                            break

                    if lru_key:
                        print("DISCARD: {}".format(lru_key))
                        del self.cache_data[lru_key]
                        del self.access_frequency[lru_key]
                        self.access_order.remove(lru_key)
                else:
                    # If access_order is empty
                    # fall back to a simple eviction strategy
                    lfu_key = items_with_min_frequency[0]
                    print("DISCARD: {}".format(lfu_key))
                    del self.cache_data[lfu_key]
                    del self.access_frequency[lfu_key]
            else:
                # If access_frequency is empty,
                # fall back to a simple eviction strategy
                if self.access_order:
                    lru_key = self.access_order[0]
                    print("DISCARD: {}".format(lru_key))
                    del self.cache_data[lru_key]
                    self.access_order.remove(lru_key)

    def get(self, key):
        """Retrieves an item from the cache based on the specified key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The item associated with the key,
            or None if the key is not found.
        """
        if key is None:
            return None

        if key in self.cache_data:
            # Update access frequency
            if key in self.access_frequency:
                self.access_frequency[key] += 1
            else:
                self.access_frequency[key] = 1

            # Update access order (move key to the end)
            if key in self.access_order:
                self.access_order.remove(key)
            self.access_order.append(key)

            return self.cache_data[key]
        else:
            return None
