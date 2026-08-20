class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        def backtrack(i, temp, mem):
            if i in mem:
                return mem[i]
            if i > len(s):
                return False
            if i == len(s):
                return True
            
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if backtrack(i + len(word), temp + word, mem):
                        mem[i] = True
                        return True
            mem[i] = False
            return False
        
    
        return backtrack(0, '', mem)
    