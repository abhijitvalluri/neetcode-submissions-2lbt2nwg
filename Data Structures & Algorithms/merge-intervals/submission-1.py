class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        c_s, c_e = intervals[0]

        for i in range(1, len(intervals)):
            si, ei = intervals[i]

            if c_s <= si <= c_e:
                c_s = min(c_s, si)
                c_e = max(c_e, ei)
            else:
                res.append([c_s, c_e])
                c_s, c_e = si, ei

        res.append([c_s, c_e])
        return res                
