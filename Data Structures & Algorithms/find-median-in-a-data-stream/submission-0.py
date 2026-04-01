class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        
    def findMedian(self) -> float:
        size = len(self.heap)
        if not size:
            return None
        if size % 2 == 0:
            mid = size // 2
            return (self.heap[mid] + self.heap[mid - 1])/2
        else:
            return self.heap[size // 2]
