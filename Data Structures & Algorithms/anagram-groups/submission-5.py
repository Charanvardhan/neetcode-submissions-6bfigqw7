from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        base = ord('a')
        for word in strs:
            key = [0 for i in range(26)]
            for char in word:
                key[ord(char) % base] += 1
            
            groups[tuple(key)].append(word)
        
        return list(groups.values())

