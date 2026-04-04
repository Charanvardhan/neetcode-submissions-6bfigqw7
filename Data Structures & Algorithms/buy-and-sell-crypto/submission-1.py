class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        n = len(prices)
        bestDay = prices[0]

        for i in range(1,n):
            if prices[i] < bestDay:
                bestDay = prices[i]
                continue
            
            sol = max(prices[i] - bestDay, sol)
        
        return sol