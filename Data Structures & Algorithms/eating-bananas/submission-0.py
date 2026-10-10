# when nb of piles = target, k = max(piles) so we eat 1 pile per hour
# when nb of piles > target, we have at most target / nb of piles hour per pile (time per pile)
#   max(pile) / time_per_pile = k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        time_per_pile = h / len(piles)
        return math.ceil(max(piles) / time_per_pile)
        