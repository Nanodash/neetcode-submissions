# without sorting:
# we maintain a ds that holds up to k elements and must stay ordered
# hint 1: the ds must just be allowed to store top k elements

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]
        