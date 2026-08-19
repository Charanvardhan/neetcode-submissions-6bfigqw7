class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = nums[0]
        op = nums[0] 

        for i in range(1, len(nums)):
            candidates = {nums[i], nums[i] * min_, nums[i]* max_}
            min_ = min(candidates)
            max_ = max(candidates)
            op = max(max_, op)

        
        return op


            
        


