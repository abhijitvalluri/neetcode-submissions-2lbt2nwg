class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)
        
        res = []

        for query in queries:
            u, v = query
            if u not in adj or u >= numCourses or v >= numCourses:
                res.append(False)
                continue
            
            queue = deque(adj[u])
            visited = set()
            visited.add(u)

            isPrereq = False
            while queue:
                crs = queue.popleft()
                if crs not in visited:
                    visited.add(crs)
                    if crs == v:
                        isPrereq = True
                        break
                    if crs in adj:
                        queue.extend(adj[crs])
            
            res.append(isPrereq)
        
        return res
