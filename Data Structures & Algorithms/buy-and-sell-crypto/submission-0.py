# for each day we have 3 choices: buy/sell/hold, but we can only make 1 buy through the list.
# a brute force solution would be to check every day considering a buy and see on what day a sell is the most lucrative => O(n^2)
# since the prices list is short (<= 100), it could be acceptable.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])

        return res      