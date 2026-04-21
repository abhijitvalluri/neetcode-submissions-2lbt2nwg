class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = {(rows - 1, cols - 1): 1}

        def dfs(r, c):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
        
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
        
        return dfs(0, 0)