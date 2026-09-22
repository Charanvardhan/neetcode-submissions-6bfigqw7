class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        op = -10001
        temp = 0
        for i in nums:
            temp += i
            op = max(temp, op)
            if temp > 0:
                continue
            else:
                temp = 0
            
        return op

        