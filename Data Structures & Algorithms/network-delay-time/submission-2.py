class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(dict)

        for u, v, t in times:
            adj[u][v] = t
        
        shortest_from_k = { i: float("inf") for i in range(1, n+1)}
        shortest_from_k[k] = 0

        queue = deque()
        queue.append((k, 0))

        while queue:
            node, t1 = queue.popleft()
            if shortest_from_k[node] < t1:
                continue
            for v in adj[node]:
                tot_time = t1 + adj[node][v]
                if tot_time < shortest_from_k[v]:
                    shortest_from_k[v] = tot_time
                    queue.append((v, tot_time))
            
        min_time_for_all = max(shortest_from_k.values())

        return -1 if min_time_for_all == float("inf") else min_time_for_all