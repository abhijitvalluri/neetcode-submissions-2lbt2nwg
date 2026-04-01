class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c_s, c_e = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            si, ei = intervals[i]
            
            if c_s <= si < c_e:
                count += 1
            else:
                c_s, c_e = si, ei
        
        return count
