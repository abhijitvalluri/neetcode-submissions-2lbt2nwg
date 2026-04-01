class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            
            q = deque([(src, 1)])
            visited = set()
            visited.add(src)

            while q:
                node, res = q.popleft()
                if node == dst:
                    return res
                for nei, weight in adj[node]:
                    if nei not in visited:
                        q.append((nei, res * weight))
                        visited.add(nei)
            
            return -1
        
        return [bfs(src, dst) for src, dst in queries]