class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        if len(piles) == h: return max_k

        speeds = [i for i in range(1, max_k)]

        k, l, r = speeds[0], 0, len(speeds) - 1

        while l <= r:
            k = speeds[(r - l) // 2]
            if self.__isFastEnough(k, h, piles):
                r = ((r - l) // 2) - 1
            else: l = ((r - l) // 2) + 1
        return k
    
    def __isFastEnough(self, speed, time, bananas) -> bool:
        spent = 0
        for b in bananas:
            spent += math.ceil(b / speed)
        return spent <= time