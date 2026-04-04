
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        sol = 0
        for i in nums:
            if i - 1 in nums:
                continue
            temp = 1
            while i + 1 in checker:
                temp += 1
                i += 1
            sol = max(temp, sol)
        
        return sol
            

        