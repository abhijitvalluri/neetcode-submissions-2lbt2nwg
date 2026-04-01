class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        shortestInter = {}

        for l, r in intervals:
            length = r - l + 1
            for i in range(l, r+1):
                if i not in shortestInter:
                    shortestInter[i] = length
                else:
                    shortestInter[i] = min(length, shortestInter[i])
        
        res = []
        for q in queries:
            if q in shortestInter:
                res.append(shortestInter[q])
            else:
                res.append(-1)

        return res