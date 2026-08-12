class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = min(cost[0], cost[1])
        dp2 = min(cost[0], cost[1])
        print(dp1, dp2)

        for i in range(3, len(cost) + 1):
            if i == 3:
                temp = min(cost[i-2], dp2 + cost[i-1])
            else:
                temp = min(dp1 + cost[i-2], dp2 + cost[i-1])
            dp1 = dp2
            dp2 = temp
        
        return dp2
            
            