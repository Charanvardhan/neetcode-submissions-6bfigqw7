class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [None for i in range(len(cost) + 2)]
        helper(0, len(cost), cost, mem)
        return min(mem[0], mem[1])
        

def helper(cur, n, cost, mem):
    if cur >= n:
        return 0

    if mem[cur] is not None:
        return mem[cur]
    
    mem[cur] = cost[cur] + min(helper(cur+1, n, cost,mem), helper(cur+2, n, cost, mem))
    return mem[cur]
    