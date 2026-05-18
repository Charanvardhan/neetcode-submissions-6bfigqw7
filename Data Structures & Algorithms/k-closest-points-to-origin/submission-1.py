import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        op = []
        distances = []

        for i in points:
            distance = math.sqrt((i[0] ** 2)+ (i[1] ** 2))
            heapq.heappush(distances, [-distance, i])
            while len(distances) > k:
                heapq.heappop(distances)
        
        while len(distances) > 0:
            op.append(heapq.heappop(distances)[1])
        return op