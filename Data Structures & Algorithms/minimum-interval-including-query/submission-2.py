class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_with_idx = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        i = 0
        heap = []
        for q, idx in queries_with_idx:
            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (length, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap:
                res[idx] = heap[0][0]
        
        return res
