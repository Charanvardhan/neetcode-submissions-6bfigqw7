class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: 1 way to decode an empty suffix
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0  # A string starting with '0' cannot be decoded
            else:
                # 1. Take a single digit
                dp[i] = dp[i + 1]
                
                # 2. Take two digits (if valid)
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
                    
        return dp[0]
        