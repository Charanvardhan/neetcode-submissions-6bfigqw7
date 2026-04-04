class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = 2**32

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                sol = min(sol, nums[mid])
                r = mid - 1

        return sol