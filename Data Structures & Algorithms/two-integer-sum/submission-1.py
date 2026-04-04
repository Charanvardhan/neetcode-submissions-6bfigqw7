class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = dict()

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in rem:
                return [rem[rest], i]
            else:
                rem[nums[i]] = i
