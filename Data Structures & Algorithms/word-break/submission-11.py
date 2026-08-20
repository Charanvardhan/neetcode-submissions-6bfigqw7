class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                wordLen = len(word)
                if s[i:i+wordLen] == word and dp[i+wordLen]:
                    dp[i] = True
                    break
        
        return dp[0]