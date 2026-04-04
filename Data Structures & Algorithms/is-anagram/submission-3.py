class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = {}
        for i in s:
            if i in sCount:
                sCount[i] += 1
                continue
                
            sCount[i] = 1
        
        for j in t:
            if j not in sCount:
                return False
            if sCount[j] == 0:
                print(sCount)
                return False
            sCount[j] -= 1
        
        print(sCount)
        return True