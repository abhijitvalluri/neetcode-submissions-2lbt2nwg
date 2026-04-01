class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pac = set()
        atl = set()

        for j in range(cols):
            pac.add((0, j))
            atl.add((rows - 1, j))
        for i in range(rows):
            pac.add((i, 0))
            atl.add((i, cols - 1))

        q = deque()
        for (x, y) in pac:
            q.append((x, y))

        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                currHeight = heights[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in pac and 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= currHeight:
                        pac.add((nx, ny))
                        q.append((nx, ny))
            
        for (x, y) in atl:
            q.append((x, y))
        
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                currHeight = heights[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in atl and 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= currHeight:
                        atl.add((nx, ny))
                        q.append((nx, ny)) 
        
        return list(pac & atl)
        