from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        # check = 2**32 - 1 

        for i in nums:
            dd[i] += 1
        for n,c in dd.items():
            freq[c].append(n)

        print(freq)
        op = []
        for l in range(len(freq)-1, -1, -1):
            for n in freq[l]:
                op.append(n)
                k -= 1
                if k == 0:
                    return op
        
