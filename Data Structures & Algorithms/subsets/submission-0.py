class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = []
        subset = []
        def backtrack( i, subset):
            op.append(subset.copy())
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1 ,subset)     
                subset.pop()
        
        backtrack( 0,subset)
            
        return op