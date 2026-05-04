from collections import defaultdict

def findKey(s):
    key = [0] * 26
    for k in s:
        idx = ord(k) % 97
        key[idx] += 1
    return tuple(key)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        # groups = defaultdict(list)
        groups = dict()
        for i in strs:
            key = findKey(i)
            if key in groups:
                groups[key].append(i)
            else:
                groups[key] = [i]
            
        return list(groups.values())