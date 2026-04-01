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
            nextNode = -1
            for i in unvisited:
                cost = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                dist[i] = min(dist[i], cost)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            node = nextNode
        return res

