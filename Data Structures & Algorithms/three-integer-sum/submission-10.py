class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        op = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]

            left = i +1
            right = n - 1

            while left < right:
                temp = nums[left] + nums[right]
                if temp == -target:
                    op.append([nums[i], nums[left], nums[right]])
                    while left+1 < n and nums[left+1] == nums[left]:
                        left += 1
                    while right - 1 > -1 and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
                elif temp > -target:
                    right -= 1
                
                else:
                    left += 1
                
        return op
            
