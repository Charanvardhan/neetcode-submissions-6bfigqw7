class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sos = set(nums)
        sol = 0
        for i in nums:
            if i-1 in sos:
                continue
            temp = 1
            while i + 1 in nums:
                temp += 1
                i += 1
            sol = max(temp, sol)
        
        return sol