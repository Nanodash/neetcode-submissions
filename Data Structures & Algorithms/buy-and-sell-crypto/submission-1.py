# for each day we have 3 choices: buy/sell/hold, but we can only make 1 buy through the list.
# a brute force solution would be to check every day considering a buy and see on what day a sell is the most lucrative => O(n^2)
# since the prices list is short (<= 100), it could be acceptable.

# if we keep in mind the lowest buying price, we can then evaluate profits in one pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]

        for p in prices:
            res = max(res, p - minPrice)
            if p < minPrice:
                minPrice = p
            

        return res      