class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        visited = set()
        minCost = float("inf")
        visited.add(src)
        
        def dfs(cur, cost, count):
            nonlocal minCost
            if count > k:
                return
            
            for nxt, price in adj[cur]:
                if nxt == dst:
                    minCost = min(cost + price, minCost)
                elif nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt, cost + price, count + 1)
                    visited.remove(nxt)
        
        dfs(src, 0, 0)
        return minCost if minCost != float("inf") else -1


