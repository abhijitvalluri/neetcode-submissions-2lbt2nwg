class TrieNode:
    def __init__(self):
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curMap = self.root
        for ch in word:
            if ch not in curMap:
                curMap[ch] = {}
            curMap = curMap[ch]
        curMap["word"] = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curMap = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for ch in curMap:
                        if ch != "word" and dfs(i + 1, curMap[ch]):
                            return True
                    return False
                else:
                    if c not in curMap:
                        return False
                    curMap = curMap[c]
            return curMap["word"]

        return dfs(0, self.root)
