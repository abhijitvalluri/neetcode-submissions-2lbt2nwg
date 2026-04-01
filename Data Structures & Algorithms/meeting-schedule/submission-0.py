"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: (i.start, i.end))

        busy_till = 0

        for inter in intervals:
            if inter.start < busy_till:
                return False
            else:
                busy_till = inter.end
        
        return True
