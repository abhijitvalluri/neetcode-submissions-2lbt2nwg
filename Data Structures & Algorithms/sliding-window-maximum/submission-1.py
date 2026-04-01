class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        for i in range(k, len(nums)):
            l = i - k
            while heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            heapq.heappush(heap, (-nums[i], i))

        while heap[0][1] < l:
            heapq.heappop(heap)
        res.append(-heap[0][0])
        return res
