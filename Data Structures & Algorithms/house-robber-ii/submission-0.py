class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        def helper(start, end):
            length = end - start
            sol = [nums[start], max(nums[start], nums[start+1])]
            for i in range(2, length):
                print(i)
                if nums[start + i] + sol[i-2] > sol[i-1]:
                    sol.append(nums[start + i] + sol[i-2])
                else:
                    sol.append(sol[i-1])
            return sol[-1]
            
        return max(helper(0, len(nums)-1), helper(1,len(nums)))
            