from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], size: int) -> List[int]:
        counter = defaultdict(int)
        heap = []
        op = []

        for i in nums:
            counter[i] += 1
        
        for k,v in counter.items():
            heapq.heappush(heap, (-v,k))
        
        for i in range(size):
            v, k = heapq.heappop(heap)
            op.append(k)
        
        return op

        
