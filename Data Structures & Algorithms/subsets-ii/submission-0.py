class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        n = len(nums)

        def dfs(i, cur):
            if i >= n:
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            while i<n-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)
            
        dfs(0, cur)
        return res
                
        
        