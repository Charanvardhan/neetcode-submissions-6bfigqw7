class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            if dp[i-1] > (nums[i] + dp[i-2]):
                dp.append(dp[i-1])
            else:
                dp.append(nums[i] + dp[i-2])

        return dp[-1]
