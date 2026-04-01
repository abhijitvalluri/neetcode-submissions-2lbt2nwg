class Solution:
    def areAdjacent(self, word1, word2):
        numDiff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                numDiff += 1
            if numDiff > 1:
                return False
        return numDiff == 1
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
    
        adj = defaultdict(list)

        for word in wordList:
            if self.areAdjacent(beginWord, word):
                adj[beginWord].append(word)
        
        for word1 in wordList:
            for word2 in wordList:
                if self.areAdjacent(word1, word2):
                    adj[word1].append(word2)

        queue = deque()
        queue.append(beginWord)
        length = 1
        visited = set()
        while queue:
            length += 1
            queueSize = len(queue)

            for _ in range(queueSize):
                word = queue.popleft()
                visited.add(word)
                for nei in adj[word]:
                    if nei == endWord:
                        return length
                    if nei not in visited:
                        queue.append(nei)
        
        return 0
