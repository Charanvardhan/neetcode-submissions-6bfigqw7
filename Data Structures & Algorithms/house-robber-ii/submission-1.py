class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def helper(start, end):
            rb1, rb2 = 0, 0
            for i in range(start, end):
                rbmax = max(rb2, rb1 + nums[i])
                rb1 = rb2
                rb2 = rbmax
            
            return rb2
        
        return max(helper(0,n-1), helper(1,n))
        