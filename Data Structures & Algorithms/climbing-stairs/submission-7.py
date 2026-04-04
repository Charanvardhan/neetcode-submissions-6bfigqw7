class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        mem = [None for i in range(n)]
        mem[-1] = 1
        mem[-2] = 2

        for i in range(n-3, -1, -1):
            mem[i] = mem[i+1] + mem[i+2]

        return mem[0]

        

