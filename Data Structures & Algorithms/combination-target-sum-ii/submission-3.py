class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def backtrack(i, cur):
            if sum(cur) == target:
                # temp = tuple(cur[:])
                res.append(cur[:])
                return
            
            if sum(cur) > target:
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:  # skip duplicates
                    continue
                cur.append(candidates[j])
                backtrack(j+1, cur)
                cur.pop()
                
                
        
        backtrack(0, cur)
        return res
        