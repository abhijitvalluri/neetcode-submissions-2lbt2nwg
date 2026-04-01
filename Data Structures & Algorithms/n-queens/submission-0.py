class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colsUsed, posDiagUsed, negDiagUsed = set(), set(), set()
        grid = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in colsUsed and r + c not in posDiagUsed and r - c not in negDiagUsed:
                    grid[r][c] = "Q"
                    colsUsed.add(c)
                    posDiagUsed.add(r + c)
                    negDiagUsed.add(r - c)
                    backtrack(r + 1)
                    grid[r][c] = "."
                    colsUsed.remove(c)
                    posDiagUsed.remove(r + c)
                    negDiagUsed.remove(r - c)
        
        backtrack(0)
        return res
        