class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        forwardPass = [nums[0]]
        for i in range(1, len(nums)):
            if forwardPass[i-1] != 0:
                forwardPass.append(nums[i]*forwardPass[i-1])
            else:
                forwardPass.append(nums[i]*1)
        
        forward= max(forwardPass)
        
        backwardPass = [0 for i in range(len(nums))]
        backwardPass[-1] = nums[-1]

        for j in range(len(nums)-2, -1, -1):
            if backwardPass[j+1] != 0:
                backwardPass[j] = nums[j] * backwardPass[j+1]
            else:
                backwardPass[j] = nums[j] * 1

        backward = max(backwardPass)

        return max(forward, backward)

        