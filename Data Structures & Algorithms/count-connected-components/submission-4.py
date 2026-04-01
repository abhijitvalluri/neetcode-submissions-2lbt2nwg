class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components
        