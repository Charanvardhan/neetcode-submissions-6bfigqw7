class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mem = dict()

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in mem:
                return mem[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                mem[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                mem[(i, buying)] = max(sell, cooldown)
            return mem[(i, buying)]
        
        return dfs(0, True)