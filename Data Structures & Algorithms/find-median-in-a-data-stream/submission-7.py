import heapq
class MedianFinder:
    def __init__(self):
        self.lhp = []
        self.rhp = []

    def addNum(self, num: int) -> None:
        lhp = self.lhp
        rhp = self.rhp
        ll = len(lhp)
        rl = len(rhp)

        if ll == rl:
            if ll == 0 or num <= -lhp[0]:
                heapq.heappush(lhp, -num)
            else:
                heapq.heappush(rhp, num)
        
        elif ll > rl:
            if num < -lhp[0]:
                heapq.heappush(rhp, -heapq.heappop(lhp))
                heapq.heappush(lhp, -num)
            else:
                heapq.heappush(rhp, num)
        else:
            if num > rhp[0]:
                heapq.heappush(lhp, -heapq.heappop(rhp))
                heapq.heappush(rhp, num)
            else:
                heapq.heappush(lhp, -num)
        

    def findMedian(self) -> float:
        lhp = self.lhp
        rhp = self.rhp
        ll = len(lhp)
        rl = len(rhp)

        if ll == rl:
            return (-lhp[0] + rhp[0]) / 2
        elif ll > rl:
            return float(-lhp[0])
        else:
            return float(rhp[0])