class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return float("inf")
            
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return cache[(r, c)]
        
        return dfs(0, 0)
