class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        
        def dfs(node, parent, visited):
            if node in visited:
                return True

            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node, visited):
                    return True
            return False

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

            if dfs(u, -1, set()):
                return [u, v]
            
        return []
