class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        reverseCounts = defaultdict(list)

        for num in counts:
            reverseCounts[counts[num]].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            for num in reverseCounts[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
