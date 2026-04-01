class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        intervals.sort()
        res = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            newInter = intervals[i]
            if newInter[0] > cur[1]:
                res.append(cur)
                cur = newInter
            else:
                cur = [cur[0], max(cur[1], newInter[1])]
        
        res.append(cur)
        return res
        