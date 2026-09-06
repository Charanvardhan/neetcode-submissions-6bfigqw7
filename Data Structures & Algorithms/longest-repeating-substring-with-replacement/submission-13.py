from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        freq = defaultdict(int)
        op =0 

        while right < n:
            freq[s[right]] += 1
            maxFreq = max(freq.values())

            validator = (right - left + 1) - maxFreq

            while validator > k:
                freq[s[left]] -= 1
                left += 1
                maxFreq = max(freq.values())

                validator = (right - left + 1) - maxFreq
            
            op = max(right - left + 1, op)
            right += 1
        
        return op

    

