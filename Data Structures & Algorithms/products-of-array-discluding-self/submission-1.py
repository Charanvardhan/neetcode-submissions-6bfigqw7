class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lr = [1]

        for i in range(n - 1):
            lr.append(lr[i]*nums[i])
        
        rl = [1] * n

        for i in range(n-1, 0, -1):
            rl[i - 1] = rl[i] * nums[i]
        
        op = []

        for i in range(n):
            op.append(lr[i]*rl[i])
        
        return op