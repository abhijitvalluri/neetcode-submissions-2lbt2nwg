class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = set()
        visited = set()

        def backtrack(r, c, node, wordSoFar):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r, c))
            char = board[r][c]
            node = node.children[char]
            wordSoFar += char
            if node.isWord:
                res.add(wordSoFar)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                backtrack(nr, nc, node, wordSoFar)
            
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                visited = set()
                backtrack(r, c, root, "")
        
        return list(res)
        