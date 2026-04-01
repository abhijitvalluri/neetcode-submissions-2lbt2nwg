class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(dict)

        for u, v, t in times:
            adj[u][v] = t
        
        shortest_from_k = {i: float('inf') for i in range(1, n + 1)}
        shortest_from_k[k] = 0
        
        q = deque()
        q.append((k, 0))

        while q:
            node, t1 = q.popleft()
            for v in adj[node]:
                tot_time = t1 + adj[node][v]
                if tot_time < shortest_from_k[v]:
                    shortest_from_k[v] = tot_time
                    q.append((v, tot_time))

        max_time = max(shortest_from_k.values())
        return max_time if max_time != float('inf') else -1
        