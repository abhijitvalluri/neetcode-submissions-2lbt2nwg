class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]
