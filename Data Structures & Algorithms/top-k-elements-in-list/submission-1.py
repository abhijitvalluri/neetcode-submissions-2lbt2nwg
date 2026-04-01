class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num in counts:
            freq[counts[num]].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
