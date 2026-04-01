class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        reverseCounts = defaultdict(list)
        for num in counts:
            reverseCounts[counts[num]].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            if i in reverseCounts:
                res.extend(reverseCounts[i])
                if len(res) == k:
                    return res
        
        return res
