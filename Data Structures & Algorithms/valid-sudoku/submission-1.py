class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, grids = [0] * 9, [0] * 9, [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = int(board[r][c])
                mask = 1 << num
                if rows[r] & mask or cols[c] & mask or grids[(r // 3) * 3 + c // 3] & mask:
                    return False
                rows[r] += mask
                cols[c] + mask
                grids[(r // 3) * 3 + c // 3] += mask
        
        return True
        