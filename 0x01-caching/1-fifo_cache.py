#!/usr/bin/env python3
"""FIFO Caching system demonstration"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A class for FIFO caching system 

    Args:
        BaseCaching (Base Class for caching): parent class template for caching
    """
    # Inherit base class contructor
    def __init__(self):
        """Contructor intialization
        """
        super().__init__()
    
    def put(self, key, item):
        """Updates the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # discard the first item put in cache (FIFO Algo)
                rm_key = next(iter(self.cache_data))
                # print DISCARD with the key discarded and a new line
                print("DISCARD: {}".format(rm_key))
                # remove the first item
                del self.cache_data[rm_key]
            self.cache_data[key] = item

    def get(self, key):
        """returns an item based on key specified"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
