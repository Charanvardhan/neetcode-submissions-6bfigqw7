from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()

        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for j in t:
            if j not in counter:
                return False
            else:
                counter[j] -= 1
            
        for k,v in counter.items():
            if v != 0:
                return False
            
        return True
 
        