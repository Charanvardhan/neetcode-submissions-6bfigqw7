from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mda = deque()
        sol = []

        for i in range(k):
            while len(mda) > 0 and mda[-1][1] < nums[i]:
                mda.pop()
            mda.append((i,(nums[i])))
        
        sol.append(mda[0][1])
        
        l = 0
        for r in range(k, len(nums)):
            while len(mda) > 0 and mda[-1][1] < nums[r]:
                mda.pop()
            mda.append((r,(nums[r])))
            if len(mda) > 0 and mda[0][0] == l:
                mda.popleft()
            sol.append(mda[0][1])
            l += 1
        
        return sol
        