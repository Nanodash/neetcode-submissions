class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        if len(piles) == h: return max_k

        speeds = [i for i in range(1, max_k)]

        k, l, r = speeds[0], 0, len(speeds) - 1

        while l <= r:
            mid = (r - l) // 2
            k = speeds[mid]

            if self.__isFastEnough(k, h, piles):
                r = mid - 1
            else: l = mid + 1

        return k
    
    def __isFastEnough(self, speed, time, bananas) -> bool:
        for b in bananas:
            spent += math.ceil(b / speed)
        return spent <= time