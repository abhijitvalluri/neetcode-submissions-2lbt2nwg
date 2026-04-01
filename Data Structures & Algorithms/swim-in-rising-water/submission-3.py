class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0,0))
        while heap:
            timeSoFar, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return timeSoFar
        
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(timeSoFar, grid[nr][nc]), nr, nc))
        
        return -1