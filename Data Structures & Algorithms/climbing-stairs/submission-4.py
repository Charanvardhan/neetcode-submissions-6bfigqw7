class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [None for i in range(n)]
        return helper(0, n, mem)

def helper(cur, n, mem):
    if cur > n:
        return 0
    if cur == n:
        return 1
    if mem[cur] is not None:
        return mem[cur]

    mem[cur] = helper(cur+1, n, mem) + helper(cur+2, n, mem)
    return mem[cur]