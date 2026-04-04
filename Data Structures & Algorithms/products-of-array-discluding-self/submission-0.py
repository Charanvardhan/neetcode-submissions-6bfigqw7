class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        # 1, -1, 0, 0, 0 | 0, 6, 6, 3, 1

        right_product = [1]
        left_product = [0 for i in range(len(nums))]
        left_product[-1] = 1

        for i in range(len(nums) - 1):
            right_product.append(nums[i]*right_product[-1])

        for j in range(len(nums)-1, 0, -1):
            left_product[j - 1] = nums[j] * left_product[j]

        sol = []

        for i in range(len(nums)):
            sol.append(left_product[i]*right_product[i])

        return sol
