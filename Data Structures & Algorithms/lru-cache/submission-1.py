class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.gen = 0


    def get(self, key: int) -> int:
        self.gen += 1
        if key not in self.cache:
            return -1
        value, _ = self.cache[key]
        self.cache[key] = (value, self.gen)
        return value


    def put(self, key: int, value: int) -> None:
        self.gen += 1
        self.cache[key] = (value, self.gen)
        if len(self.cache) > self.capacity:
            lru = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[lru]


