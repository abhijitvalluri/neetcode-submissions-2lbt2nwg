class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            cur = root

            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for ch in cur.children:
                        return dfs(i + 1, cur.children[ch])
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word 
