class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        n = len(prices)
        op = 0
        while r < n:
            if prices[r] >= prices[l]:
                op = max(op, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return op