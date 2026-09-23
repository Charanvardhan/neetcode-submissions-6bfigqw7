class Solution:
    def canJump(self, nums: List[int]) -> bool:
        itr = 1
        curMax = nums[0]
        n = len(nums) - 1

        while itr <= curMax and curMax < n:
            curMax = max(itr + nums[itr], curMax)
            itr += 1
        
        if curMax >= n:
            return True
        return False


        