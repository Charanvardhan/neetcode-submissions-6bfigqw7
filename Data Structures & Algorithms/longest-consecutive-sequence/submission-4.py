class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        op = 0

        for i in nums:
            if i - 1 not in hashset:
                sequence = 1
                while i+1 in hashset:
                    sequence += 1
                    i += 1
                op = max(op, sequence)
        
        return op
        