from heapq import *


class MedianFinder(object):
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        lo, hi = self.heaps
        heappush(lo, -num)
        heappush(hi, -heappop(lo))
        if len(lo) < len(hi):
            heappush(lo, -heappop(hi))

    def findMedian(self) -> float:
        lo, hi = self.heaps
        if len(lo) > len(hi):
            return float(-lo[0])
        else:
            return (hi[0] - lo[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
# obj.addNum(9)
# obj.addNum(-10)
print(obj.heaps)
print(obj.findMedian())
