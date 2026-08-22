class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        memo = {}

        def backtrack(cur, temp):
            if (cur, temp) in memo:
                return memo[(cur, temp)]
            if temp == target:
                return True
            if cur == len(nums) or temp > target:
                return False

            result = backtrack(cur + 1, temp) or backtrack(cur + 1, temp + nums[cur])
            memo[(cur, temp)] = result
            return result

        return backtrack(0, 0)