class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        unvisited = set(range(n))
        dist = [float("inf")] * n
        res = 0
        node = 0

        while len(unvisited) > 1:
            visited.add(node)
            unvisited.remove(node)
            for i in unvisited:
                cost = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                dist[i] = min(dist[i], cost)
            
            minDist = float("inf")
            for i in unvisited:
                if dist[i] < minDist:
                    minDist = dist[i]
                    node = i
            res += minDist
        return res

