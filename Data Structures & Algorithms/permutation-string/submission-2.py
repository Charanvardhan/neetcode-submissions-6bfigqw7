from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashs1 = defaultdict(int)

        for i in s1:
            hashs1[i] += 1
        
        hashs2 = defaultdict(int)

        st = 0
        en = len(s1)
        for i in range(en):
            hashs2[s2[i]] += 1

        while en < len(s2):
            if hashs1 == hashs2:
                return True
            
            hashs2[s2[st]] -= 1
            hashs2[s2[en]] += 1
            if hashs2[s2[st]] == 0:
                del hashs2[s2[st]]
            en += 1
            st += 1
        
        if hashs1 == hashs2:
            return True
        
        return False

