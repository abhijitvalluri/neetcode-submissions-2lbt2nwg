class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest_time = defaultdict(dict)

        for u, v, t in times:
            shortest_time[u][v] = t
        
        q = deque()
        q.append((k, 0))

        while q:
            node, t1 = q.popleft()
            for v in shortest_time[node]:
                tot_time = t1 + shortest_time[node][v]
                if tot_time < shortest_time[k][v]:
                    shortest_time[k][v] = tot_time
                    q.append((v, tot_time))
        
        if len(shortest_time[k]) < n - 1:
            return -1
        
        return max(shortest_time[k].values())
        