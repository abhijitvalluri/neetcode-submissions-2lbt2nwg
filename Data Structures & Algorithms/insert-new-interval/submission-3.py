class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        delete_from, delete_till = 0, 0
        delete = False
        start, end = newInterval

        for i, inter in enumerate(intervals):
            if inter[0] <= start <= inter[1]:
                delete_from = i
                start = inter[0]
                delete = True
                break
            elif start < inter[0]:
                delete_from = i
                break
        
        for i in range(delete_from, len(intervals)):
            s, e = intervals[i]
            if s <= end <= e:
                delete_till = i
                delete = True
                end = e
                break
            elif end < s:
                delete_till = i - 1
                break

        if delete_from <= delete_till:
            return intervals[:delete_from] + [[start, end]] + intervals[delete_till + 1:]
        else:
            intervals.insert(delete_from, [start, end])
            return intervals       
            