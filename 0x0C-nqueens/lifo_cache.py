#!/usr/bin/python3
"""LIFOCache class"""


class LIFOCache():
    """LIFOCache class inherit from BaseCaching"""

    def __init__(self):
        """initialize"""
        self.cache_data = {}
        self.key_list = []
        self.result = []

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)

    def pop_lifo(self):
        """Pop item LIFO
        """
        x = self.key_list.pop(-1)
        y = self.cache_data.get(x)
        self.cache_data.pop(x)
        return {x: y}

    def put(self, key, item):
        """ Add an item in the cache according LIFO Algorithm
        """
        if key is None or item is None:
            return
        if key in self.key_list:
            self.key_list.remove(key)
        self.cache_data.update({key: item})
        self.key_list.append(key)
