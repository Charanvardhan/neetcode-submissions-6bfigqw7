class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sol = 1
        for i in range(len(nums)):
            sol = max(sol, helper(nums, i, 1))
        return sol

def helper(nums, i, length):
    best = length

    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            currentLength = helper(nums, j, length+1)
            best = max(best, currentLength)
        
    return best
        
        
                
            