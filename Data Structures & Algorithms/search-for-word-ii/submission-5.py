class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self

        for ch in word:
            if ch not in self.children:
                self.children[ch] = TrieNode()
            cur = self.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode

        for word in words:
            root.addWord(word)

        res = set()
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node, wordSoFar):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r, c))
            ch = board[r][c]
            node = node.children[ch]
            wordSoFar.append(ch)
            if node.isWord:
                res.add("".join(wordSoFar))

            dfs(r + 1, c, node, wordSoFar)
            dfs(r - 1, c, node, wordSoFar)
            dfs(r, c + 1, node, wordSoFar)
            dfs(r, c - 1, node, wordSoFar)
            wordSoFar.pop()
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, [])
        
        return list(res)
