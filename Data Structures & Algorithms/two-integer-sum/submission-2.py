class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = dict()
        for i in range(len(nums)):
            req = target - nums[i]
            if req in rem:
                return [rem[req], i]
            else:
                rem[nums[i]] = i
        