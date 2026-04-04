from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1 
        
        for j in t:
            hashmap[j] -= 1
        
        print(hashmap)
        for keys in hashmap:
            if hashmap[keys] != 0:
                return False
        
        return True