class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(helper(nums, 0, len(nums) - 1), helper(nums, 1, len(nums)))
        
    
def helper(nums, s, e):
    if len(nums) == s:
        return 0
    n1 = 0
    n2 = nums[s]

    for i in range(s+1, e):
        temp = max(n2, n1 + nums[i])
        n1 = n2
        n2 = temp
    
    return n2