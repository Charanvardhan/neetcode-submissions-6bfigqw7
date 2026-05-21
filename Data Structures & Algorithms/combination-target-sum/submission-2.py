class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i, cur):
            if sum(cur) > target:
                return
            if sum(cur) == target:
                res.append(cur[:])
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j, cur)
                cur.pop()
                # backtrack(j + 1, cur)
        
        backtrack(0, cur)

        return res

        