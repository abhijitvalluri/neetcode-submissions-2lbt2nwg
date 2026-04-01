class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        m, n = len(s), len(p)

        def dfs(i, j):
            if j == n:
                return i == m
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            hasMatch = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (hasMatch and dfs(i + 1, j))
            elif hasMatch:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = False
            
            return cache[(i, j)]
        
        return dfs(0, 0)
