class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        INF = 2 ** 31 - 1

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == INF:
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
