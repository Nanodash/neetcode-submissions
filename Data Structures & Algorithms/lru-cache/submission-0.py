# we need to maintain usage status of each keys
# hashmap could work, but linked-list would make it easier if order it by usage
# linkedlist implem:
#   when add, we put in head
#   when get, we put in head too
#   when capacity hit, we remove tail
# i struggle with how i could identify by key a node in the list, falling back to hashmap implem
#
#
# {1: (10, 2), 2: (20, 1), 3: (30, 1)
# 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(tuple)
        self.gen = 0
        

    def get(self, key: int) -> int:
        self.gen += 1
        if key not in self.cache:
            return -1
        valueWithCount = self.cache[key]
        self.cache[key] = (valueWithCount[0], self.gen)
        return valueWithCount[0]
        

    def put(self, key: int, value: int) -> None:
        self.gen += 1
        if key not in self.cache:
            self.cache[key] = (value, self.gen)
            if len(self.cache) > self.capacity:
                lru = min(self.cache, key=lambda k: self.cache[k][1])
                del self.cache[lru]
        else: self.cache[key] = (value, self.gen)

