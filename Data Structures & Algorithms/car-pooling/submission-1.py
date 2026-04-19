class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        load = 0
        minHeap = []

        for trip in trips:
            numPass, src, dst = trip
            # We are currently at src location. All passengers who get off at or before src need to be removed from load
            while minHeap and minHeap[0][0] <= src:
                load -= heapq.heappop(minHeap)[1]
            
            if numPass + load > capacity:
                return False
            else:
                load += numPass
                heapq.heappush(minHeap, (dst, numPass))
        
        return True