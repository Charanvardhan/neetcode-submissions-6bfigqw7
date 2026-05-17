from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        freq = sorted(freq.items(), key= lambda item:item[1], reverse=True)
        op = []
        for key,v in freq:
            if k == 0:
                break
            op.append(key)
            k -= 1   

        return op     