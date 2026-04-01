class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            pathLen = 1
            points = [(r + dr, c + dc) for dr, dc in dirs]
            maxDirLength = 0

            for x, y in points:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[r][c]:
                    maxDirLength = max(maxDirLength, dfs(x, y))
            
            cache[(r, c)] = 1 + maxDirLength
            return cache[(r, c)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        
        return res
