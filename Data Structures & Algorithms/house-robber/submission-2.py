class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = 0
        n2 = nums[0]

        for i in range(1, len(nums)):
            temp = max(n2, n1 + nums[i])
            n1 = n2
            n2 = temp
        
        return n2

        