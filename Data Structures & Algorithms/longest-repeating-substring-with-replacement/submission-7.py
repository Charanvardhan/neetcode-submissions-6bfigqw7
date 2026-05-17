class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqTable = [0] * 26
        l = 0
        r = 0
        n = len(s)
        sol = 0
        
        while r<n:
            idx = ord(s[r]) % ord('A')
            freqTable[idx] += 1

            while (r-l+1) - max(freqTable) > k:
                idx = ord(s[l]) % ord('A')
                freqTable[idx] -= 1
                l += 1
            
            sol = max(sol, r - l + 1)
            r += 1

        return sol