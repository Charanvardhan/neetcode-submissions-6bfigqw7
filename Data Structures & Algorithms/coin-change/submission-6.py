class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sol = [float('inf') for i in range(amount + 1)]
        sol[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (coin - i) == 0:
                    sol[i] = 1
                elif (coin - i) > 0:
                    continue
                else:
                    sol[i] = min(sol[i], 1+sol[i-coin])
                
        return -1 if sol[-1] == float('inf') else sol[-1]