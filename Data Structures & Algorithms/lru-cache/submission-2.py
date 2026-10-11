
class Node:

    def __init__(self, key, val, prev = None, next = None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.lru = self.mru = Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    # remove from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert mru in list
    def insert(self, node):
        prev, next = self.mru.prev, self.mru
        prev.next = next.prev = node
        node.next, node.prev = next, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]


