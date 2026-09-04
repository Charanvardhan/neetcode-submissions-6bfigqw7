from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n+1)]
        counter = defaultdict(int)

        for i in nums:
            counter[i] += 1
        
        for n,c in counter.items():
            bucket[c].append(n)
        op = []
        temp = 0
        for i in range(len(bucket) - 1, 0, -1):
            for key in bucket[i]:
                if temp == k:
                    return op
                op.append(key)
                temp += 1
        
        return op
                

        


        
        