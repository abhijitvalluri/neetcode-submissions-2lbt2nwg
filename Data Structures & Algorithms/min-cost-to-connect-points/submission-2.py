class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [float("inf")] * n
        visited = set()
        edges, res = 0, 0

        while edges < n - 1:
            visited.add(node)
            nextNode = -1
            for i in range(n):
                if i in visited:
                    continue
                curDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            edges += 1
            node = nextNode
        
        return res