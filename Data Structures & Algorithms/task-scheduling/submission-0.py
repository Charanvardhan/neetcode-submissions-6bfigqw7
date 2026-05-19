import heapq
from collections import deque, defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Q = deque()
        time = 0
        freq = defaultdict(int)

        for i in tasks:
            freq[i] += 1
        
        maxHeap = [[-v, k] for k,v in freq.items()]
        heapq.heapify(maxHeap)
        print(maxHeap)

        while len(maxHeap) != 0 or len(Q) != 0:
            if len(maxHeap) == 0 and Q[0][1] != time:
                    time += 1
                    continue
            
            if len(Q) > 0 and Q[0][1] == time:
                left = Q.popleft()
                heapq.heappush(maxHeap, left[0])
            
            nextTask = heapq.heappop(maxHeap)
            nextTask[0] += 1
            if nextTask[0] < 0:
                nextAvailable = time + n + 1
                Q.append([nextTask, nextAvailable])
            time += 1
        
        return time 
        