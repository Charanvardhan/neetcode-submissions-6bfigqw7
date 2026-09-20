class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        op = 0
        left = 0
        right = 1

        while right < n:
            if prices[right] < prices[left]:
                left = right
            else:
                op = max(prices[right] - prices[left], op)
            right += 1
            
        return op
        