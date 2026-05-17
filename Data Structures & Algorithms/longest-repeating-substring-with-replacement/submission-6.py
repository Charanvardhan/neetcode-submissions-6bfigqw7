from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sol = 1
        n = len(s)

        for i in range(n):
            temp = defaultdict(int)
            temp[s[i]] += 1
            maxFreq = 1
            
            for j in range(i+1, n):
                temp[s[j]] += 1
                maxFreq = max(maxFreq, temp[s[j]])
                subLen = j - i + 1

                print(subLen - maxFreq)
                if subLen - maxFreq > k:
                    break
                
                sol = max(sol, subLen)
            
        return sol
        