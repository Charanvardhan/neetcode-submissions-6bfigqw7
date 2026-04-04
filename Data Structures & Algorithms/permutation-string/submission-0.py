def getFrequency(s):
    sol = [0] * 26
    for i in s:
        sol[ord(i) % ord('a')] += 1
    
    return tuple(sol)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        permutation = getFrequency(s1)
        i = 0
        j = len(s1)
        
        while j < len(s2) + 1:
            if getFrequency(s2[i:j]) == permutation:
                return True
            else:
                j += 1
                i+=1
        
        return False
        