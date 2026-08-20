class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        def backtrack(prev,cur, mem):
            if (prev, cur) in mem:
                return mem[(prev, cur)]
            best = 0

            for i in range(cur, len(nums)):
                if prev == -1 or nums[prev] < nums[i]:
                    best = max(best, backtrack(i, i+1, mem) + 1)
                
            mem[(prev, cur)] = best    
            return best
        
        
        return backtrack(-1, 0, mem)

        #O(2^n)T &O(n)