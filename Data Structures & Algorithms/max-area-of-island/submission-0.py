class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            area = 1
            grid[i][j] = 0
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        area += 1
                        grid[nx][ny] = 0
                        q.append((nx, ny))
            
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    res = max(res, area)
        
        return res
        