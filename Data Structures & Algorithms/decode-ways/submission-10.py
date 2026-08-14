class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty prefix — one way to decode nothing

        for i in range(1, n + 1):
            # single-digit contribution
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # two-digit contribution
            if i >= 2 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
            

            

        