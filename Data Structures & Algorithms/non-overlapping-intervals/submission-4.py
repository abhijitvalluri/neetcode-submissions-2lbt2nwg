class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            if newStart >= prevEnd:
                prevEnd = newEnd
            else:
                res += 1
                prevEnd = min(prevEnd, newEnd)
        
        return res