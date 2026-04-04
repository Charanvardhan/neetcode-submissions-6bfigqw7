class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        memo = [-1 for i in range(amount + 1)]
        helper(coins, amount, memo)
        
        if memo[0] == float('inf'):
            return -1
        
        return memo[0]
        

def helper(coins, amount, memo, temp=0):
    if temp > amount:
        return float('inf')
    
    if temp == amount:
        return 0

    if memo[temp] != -1:
        return memo[temp]

    best = float('inf')
    
    for i in coins:
        combination = helper(coins, amount, memo, temp + i)
        if combination != float('inf'):
            best = min(best, 1 + combination)
    
    memo[temp] = best
    return best