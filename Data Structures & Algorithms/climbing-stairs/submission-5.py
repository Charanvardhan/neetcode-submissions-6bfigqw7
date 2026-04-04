class Solution:
    def climbStairs(self, n: int) -> int:
        # mem = [None for i in range(n)]
        # mem[-1] = 1
        # mem[-2] = 2

        # for i in range(n, 1, -1):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

