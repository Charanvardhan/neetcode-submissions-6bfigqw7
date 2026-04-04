class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for word in wordDict:
                m = len(word)
                if m > i:
                    continue
                if s[i - m: i] == word and dp[i-m]:
                    dp[i] = True
        
        return dp[-1]
        