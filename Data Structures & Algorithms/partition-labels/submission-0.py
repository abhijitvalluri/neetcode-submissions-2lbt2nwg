class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        res = []

        split = 0
        partial = defaultdict(int)
        for ch in s:
            split += 1
            partial[ch] += 1
            canSplit = True
            for c in partial:
                if partial[c] < counts[c]:
                    canSplit = False
                    break
            if canSplit:
                res.append(split)
                split = 0
                partial = defaultdict(int)
        return res
        