class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)

        def dfs(cur, nums):
            if len(cur) == n:
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                cur.append(nums[i])
                dfs(cur, nums[:i] + nums[i+1:])
                cur.pop()
            
        dfs(cur, nums)
    
        return res