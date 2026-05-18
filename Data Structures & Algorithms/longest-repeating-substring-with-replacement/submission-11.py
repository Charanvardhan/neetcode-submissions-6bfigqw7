from collections import defaultdict

def freqCount(freq, key):
    total = 0

    for i in freq:
        total += freq[i]
    print (total, freq[key])
    return total - max(freq.values()) 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        r = 0
        op = 0
        n = len(s)

        while r < n:
            freq[s[r]] += 1
            print(freq)
            temp = freqCount(freq, s[l])
        
            while temp > k:
                freq[s[l]] -= 1
                l += 1
                temp = freqCount(freq, s[l])
            
            op = max(op, r - l + 1)
            r += 1
                

        return op
        
        