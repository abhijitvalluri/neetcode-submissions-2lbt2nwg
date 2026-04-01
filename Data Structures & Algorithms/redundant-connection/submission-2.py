class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True

            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
            
        return []
