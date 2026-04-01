class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            dist = 0

            while queue:
                dist += 1
                queueSize = len(queue)
                for _ in range(queueSize):
                    r, c = queue.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and grid[nr][nc] != 0:
                            if grid[nr][nc] > dist:
                                grid[nr][nc] = dist
                                queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)
        