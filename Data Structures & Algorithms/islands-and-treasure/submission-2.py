class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        
        dist = 0
        while queue:
            queueSize = len(queue)
            for _ in range(queueSize):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            dist += 1
