# at each step if 2 stones or more, we want to take 2 heaviest stones; so we need some kind of sorting.
# sorting on each step would be m * nlog(n) which is not ideal.
# maxheap? pop twice then add result
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-w for w in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1, stone2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if stone1 < stone2:
                heapq.heappush(maxHeap, -(stone2 - stone1))
            elif stone1 > stone2:
                heapq.heappush(maxHeap, -(stone1 - stone2))

        return -maxHeap[0] if maxHeap else 0