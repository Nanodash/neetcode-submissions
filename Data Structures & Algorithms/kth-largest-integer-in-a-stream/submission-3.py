class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.capHeap(self.nums, self.k)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.capHeap(self.nums, self.k)
        return self.nums[0]
        
    def capHeap(self, heap, k):
        if len(heap) > k:
            heapq.heappop(heap)

