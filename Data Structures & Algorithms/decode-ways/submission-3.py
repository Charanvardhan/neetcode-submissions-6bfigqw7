class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)

        def dfs(i):
            if i in memo:          # ✅ use memo
                return memo[i]

            if i == n:
                return 1
            
            if s[i] == "0":
                return 0
            
            ways = dfs(i+1)

            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            
            memo[i] = ways
        
            return ways
        
        return dfs(0)