class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        if len(piles) == h: return max_k


        l, r = 1, max_k

        res = -1

        while l <= r:
            mid = l + (r - l) // 2

            if self.__isFastEnough(mid, h, piles):
                res = mid
                r = mid - 1
            else: l = mid + 1

        return res
    
    def __isFastEnough(self, speed, time, bananas) -> bool:
        spent = 0
        for b in bananas:
            spent += math.ceil(b / speed)
        return spent <= time