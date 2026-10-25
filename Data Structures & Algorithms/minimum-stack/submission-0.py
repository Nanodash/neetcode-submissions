class MinStack:

    def __init__(self):
        self.heap = []
        

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        

    def pop(self) -> None:
        heapq.heappop(self.heap)
        

    def top(self) -> int:
        return self.heap[-1]

    def getMin(self) -> int:
        return self.heap[0]
