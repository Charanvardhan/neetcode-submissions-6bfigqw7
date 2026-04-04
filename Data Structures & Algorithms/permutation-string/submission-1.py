def getFrequency(s, i, j):
    sol = [0] * 26
    for i in range(i,j):
        sol[ord(s[i]) % ord('a')] += 1
    
    return tuple(sol)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        permutation = getFrequency(s1, 0, len(s1))
        i = 0
        j = len(s1)
        
        while j < len(s2) + 1:
            if getFrequency(s2,i,j) == permutation:
                return True
            else:
                j += 1
                i += 1
        
        return False
        