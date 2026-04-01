class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def search(idx, pos, visited):
            if idx == len(word):
                return True

            r, c = pos
            ch = word[idx]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == ch:
                    visited.add((nr, nc))
                    if search(idx + 1, (nr, nc), visited):
                        return True
                    visited.remove((nr, nc))
            return False
                    

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r, c))
                    if search(1, (r, c), visited):
                        return True
        
        return False
