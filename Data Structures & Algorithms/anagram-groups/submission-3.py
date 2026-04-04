from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            sol[key].append(word)
        
        return list(sol.values())
