class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []

        for i in range(n - 2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]

            while j < k:
                temp = nums[j] + nums[k]
                if temp > target:
                    k -= 1
                elif temp < target:
                    j += 1
                else:
                    sol.append([-target, nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return sol

                

        