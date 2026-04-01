class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        def areAdjacent(word1, word2):
            numDiff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    numDiff += 1
                if numDiff > 1:
                    return False
            return numDiff == 1

        adj = defaultdict(list)
        for word in wordList:
            if areAdjacent(beginWord, word):
                adj[beginWord].append(word)
        
        for word1 in wordList:
            for word2 in wordList:
                if word1 != word2 and areAdjacent(word1, word2):
                    adj[word1].append(word2)

        queue = deque()
        queue.append(beginWord)
        visited = set()
        length = 1

        while queue:
            length += 1
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                visited.add(word)
                for nei in adj[word]:
                    if nei not in visited:
                        if nei == endWord:
                            return length
                        queue.append(nei)
        
        return 0
