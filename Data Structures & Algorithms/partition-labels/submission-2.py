class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {c: idx for idx, c in enumerate(s)}
        res = []
        size = end = 0

        for idx, ch in enumerate(s):
            size += 1
            end = max(end, lastIndex[ch])
            if idx == end:
                res.append(size)
                size = 0
        
        return res
