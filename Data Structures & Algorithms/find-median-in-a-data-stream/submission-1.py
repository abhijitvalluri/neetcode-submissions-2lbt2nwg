class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        smallLen = len(self.small)
        largeLen = len(self.large)

        if smallLen > largeLen:
            return -self.small[0]
        elif largeLen > smallLen:
            return self.large[0]
        else:
            return (self.large[0] - self.small[0])/2
