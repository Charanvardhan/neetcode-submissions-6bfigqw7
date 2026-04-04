class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        helper(nums, target, op)
        return op

def helper(nums, target, op, check=[]):
    if sum(check) > target:
        return

    if sum(check) == target:
        op.append(check[:])
        return

    for i in range(len(nums)):
        check.append(nums[i])
        helper(nums[i:], target, op, check)
        check.pop()


        