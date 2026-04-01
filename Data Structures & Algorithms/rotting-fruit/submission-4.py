class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rotten = set()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        q = deque()
        for loc in rotten:
            q.append(loc)

        minutes = 0
        while fresh and q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        
        return -1 if fresh else minutes
