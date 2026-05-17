from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        op = 0
        for i in nums:
            if i - 1 in unique:
                continue
            temp = i
            count = 1
            while temp + 1 in unique:
                count += 1
                temp += 1
            
            op = max(op, count)
        
        return op
