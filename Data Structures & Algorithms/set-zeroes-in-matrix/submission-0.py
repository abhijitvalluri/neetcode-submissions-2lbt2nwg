class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRow = False
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        zeroRow = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0            

        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0
        
        for c in range(cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        
        if zeroRow:
            for c in range(cols):
                matrix[0][c] = 0

        
        