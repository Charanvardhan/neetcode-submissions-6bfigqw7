class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        l = 0
        for r in range(k, len(nums)+1):
            temp = -10000
            for i in range(l, r):
                temp = max(temp, nums[i])
            sol.append(temp)
            l += 1
        
        return sol
        