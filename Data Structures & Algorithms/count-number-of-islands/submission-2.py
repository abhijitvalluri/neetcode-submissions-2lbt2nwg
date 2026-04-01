class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def visitIsland(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    visitIsland(r, c)
        
        return res
        