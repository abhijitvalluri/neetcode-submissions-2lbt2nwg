class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        cur = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            newInter = intervals[i]
            if newInter[0] >= cur[1]:
                cur = newInter
            else:
                res += 1
        
        return res