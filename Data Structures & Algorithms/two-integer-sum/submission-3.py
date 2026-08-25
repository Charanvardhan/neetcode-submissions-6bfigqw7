class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = dict()

        for i in range(len(nums)):
            if target - nums[i] in remaining:
                return [remaining[target - nums[i]], i]
            remaining[nums[i]] = i
        