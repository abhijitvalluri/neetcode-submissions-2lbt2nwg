class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        cache = {}
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            minTime = float("inf")
            curHeight = grid[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    minTime = min(minTime, max(curHeight, dfs(nr, nc, visited)))
                    visited.remove((nr, nc))
            cache[(r, c)] = minTime
            return minTime
        
        visited = {(0, 0)}
        return dfs(0,0, visited)
