class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2: # not lexicographic order
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visited = {}
        res = []

        def dfs(ch):
            if ch in visited:
                return visited[ch]
            
            visited[ch] = True

            for nei in adj[ch]:
                if dfs(nei):
                    return True
                
            visited[ch] = False
            res.append(ch)
            return False
        
        for ch in adj:
            if dfs(ch):
                return ""
            
        res.reverse()
        return "".join(res)
        