"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [inter.start for inter in intervals]
        ends = [inter.end for inter in intervals]
        starts.sort()
        ends.sort()

        count = 0
        res = 0
        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        
        return res

        