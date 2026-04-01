class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            st1 = -heapq.heappop(heap)
            st2 = -heapq.heappop(heap)

            if st1 > st2:
                heapq.heappush(heap, st2 - st1)
        return 0 if not heap else -heap[0]
        