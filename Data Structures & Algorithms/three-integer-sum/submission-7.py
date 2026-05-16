def allTwoSums(nums, i, j, k, triplets):
    target = -nums[i]
    while j < k:
        total = nums[j] + nums[k]
        if total == target:
            triplets.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
            while j < k and nums[j-1] == nums[j]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1
        elif total > target:
            k -= 1
        else:
            j += 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            allTwoSums(nums, i, i+1, n-1, triplets)
        return triplets
        