class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for p in points:
            heapq.heappush_max(closest, (self.distanceFromOrigin(p), p))
            if len(closest) > k:
                heapq.heappop_max(closest)
        return [p for _, p in closest]
    
    def distanceFromOrigin(self, p: List[int]):
        return math.sqrt(math.pow(p[0], 2) + math.pow(p[1], 2))