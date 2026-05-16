from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            key = [0] * 26
            for i in str:
                key[ord(i) % ord('a')] += 1
            
            anagrams[tuple(key)].append(str)
        
        return list(anagrams.values())
                

            
        return []