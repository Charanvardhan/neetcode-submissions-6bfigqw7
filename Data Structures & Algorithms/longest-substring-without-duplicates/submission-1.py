class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sol = 0

        for i in range(len(s)):
            uniqueChar = {s[i]}
            for j in range(i+1, len(s)):
                if s[j] in uniqueChar:
                    sol = max(sol, len(uniqueChar))
                    uniqueChar = set()
                
                uniqueChar.add(s[j])
            
            sol = max(sol, len(uniqueChar))
        
        return sol
                
                