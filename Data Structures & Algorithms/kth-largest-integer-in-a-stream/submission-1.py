# using heap 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        heapq.heapify(self.stream)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        return self.stream[-self.k]
        
