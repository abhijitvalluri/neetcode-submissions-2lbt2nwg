class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        extra_edge = []

        for a, b in edges:
            if b not in adj[a]:
                adj[a].add(b)
                adj[b].add(a)

                for c in adj[a]:
                    adj[c].add(b)
                    adj[b].add(c)
                
                for c in adj[b]:
                    adj[c].add(a)
                    adj[a].add(c)
            else:
                extra_edge = [a, b]

        return extra_edge
