class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        dist = 0

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            size = len(q)

            for _ in range(size):
                x, y = q.popleft()
                grid[x][y] = dist
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            
            dist += 1
        