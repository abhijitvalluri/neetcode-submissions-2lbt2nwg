class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for num in counts:
            heapq.heappush(heap, (-counts[num], num))
        
        res = []
        while len(res) < k:
            num = heapq.heappop(heap)[1]
            res.append(num)
        
        return res
