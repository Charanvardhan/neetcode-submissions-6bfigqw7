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

        if ll == 0:
            heapq.heappush(lhp, -num)
            return
        # if rl == 0:
        #     if num < -lhp[0]:
        #         temp = -heapq.heappop(lhp)
        #         heapq.heappush(rhp, temp)
        #         heapq.heappush(lhp, -num)
        #     else:
        #         heapq.heappush(rhp, num)
        #     return

        if ll == rl:
            if ll == 0 or num <= -lhp[0]:
                heapq.heappush(lhp, -num)
            else:
                heapq.heappush(rhp, num)
        
        elif ll > rl:
            if num < -lhp[0]:
                temp = -heapq.heappop(lhp)
                heapq.heappush(rhp, temp)
                heapq.heappush(lhp, -num)
            else:
                heapq.heappush(rhp, num)
        else:
            if num > rhp[0]:
                temp = heapq.heappop(rhp)
                heapq.heappush(rhp, num)
                heapq.heappush(lhp, -temp)
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