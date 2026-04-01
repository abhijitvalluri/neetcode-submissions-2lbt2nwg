class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def visitIsland(i, j): 
            grid[i][j] = "2"
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = 2
                        q.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    visitIsland(i, j)

        return count
   