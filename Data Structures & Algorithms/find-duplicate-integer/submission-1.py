class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                return abs(nums[i])

        
        return
        