class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()

        for i in range(cols):
            if board[0][i] == 'O':
                q.append((0, i))
                board[0][i] = 'T'
            if board[rows - 1][i] == 'O':
                q.append((rows - 1, i))
                board[rows - 1][i] = 'T'
            
        for i in range(1, rows - 1):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'T'
            if board[i][cols - 1] == 'O':
                q.append((i, cols - 1))
                board[i][cols - 1] = 'T'
        
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 'O':
                        board[ni][nj] = 'T'
                        q.append((ni, nj))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        