# each day, 3 choices: buy/sell, skip; we must compute max profit for each path
# we must know if we are currently holding a coin
# whether we sell or not depends on the next days to maximize profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def maximize(i, hold, pnl):
            if i >= len(prices): return pnl
            if hold:
                # sell or hold
                return max(
                    maximize(i+2, False, pnl + prices[i]),
                    maximize(i+1, True, pnl)
                )
            else:
                # buy or skip
                return max(
                    maximize(i+1, True, pnl - prices[i]),
                    maximize(i+1, False, pnl)
                )
        
        return maximize(0, False, 0)
        