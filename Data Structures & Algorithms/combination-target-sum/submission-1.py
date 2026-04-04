class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        i = 0
        
        def helper(i, check=[]):
            if sum(check) > target:
                return

            if sum(check) == target:
                print(check)
                op.append(check[:])
                return

            for j in range(i, len(nums)):
                check.append(nums[j])
                helper(j, check)
                check.pop()

        helper(i)
        return op








#         op = []
#         helper(nums, target, op)
#         return op

# def helper(nums, target, op, check=[]):
#     if sum(check) > target:
#         return

#     if sum(check) == target:
#         op.append(check[:])
#         return

#     for i in range(len(nums)):
#         check.append(nums[i])
#         helper(nums[i:], target, op, check)
#         check.pop()


        