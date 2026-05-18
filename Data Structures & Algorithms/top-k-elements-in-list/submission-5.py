from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        op = []

        for i in nums:
            freq[i] += 1
        
        buckets = [[] for i in range(n)]

        for key, value in freq.items():
            buckets[value - 1].append(key)
        
        for i in range(n-1, -1, -1):
            if len(buckets[i]) > 0:
                temp = 0
                while k > 0 and temp < len(buckets[i]):
                    op.append(buckets[i][temp])
                    k -= 1
                    temp += 1

        return op
                
            
        