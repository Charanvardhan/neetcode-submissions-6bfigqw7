class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        memo = {}

        def backtrack(cur, remaining):
            if (cur, remaining) in memo:
                return memo[(cur, remaining)]
            if remaining == 0:
                return True
            if cur == len(nums) or remaining < 0:
                return False

            result = backtrack(cur + 1, remaining) or backtrack(cur + 1, remaining - nums[cur])
            memo[(cur, remaining)] = result
            return result

        return backtrack(0, target)