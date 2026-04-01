class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == len(s):
                if j == len(p) - 1:
                    return False
                else:
                    if p[j + 1] == '*':
                        cache[(i, j)] = dfs(i, j + 2)
                    else:
                        cache[(i, j)] = False
                    return cache[(i, j)]
            
            if p[j].isalpha() and s[i] != p[j]:
                return False # invalid pattern
                        
            if s[i] == p[j] or p[j] == '.':
                cache[(i, j)] = dfs(i + 1, j + 1)
            else: # p[j] == '*'
                if j == 0 or p[j - 1] == '*':
                    return False # invalid pattern
                elif p[j - 1].isalpha() and p[j - 1] != s[i]:
                    return False
                else: # p[j - 1] == '.' or p[j - 1] == s[i], so it is a match
                    cache[(i, j)] = dfs(i + 1, j) or dfs(i + 1, j + 1) or dfs(i, j + 1)
            return cache[(i, j)]
        
        return dfs(0, 0)
