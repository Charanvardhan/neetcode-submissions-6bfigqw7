import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)
            if y -x > 0:
                heapq.heappush(stones, -(y-x))

        return -stones[0] if len(stones) > 0 else 0