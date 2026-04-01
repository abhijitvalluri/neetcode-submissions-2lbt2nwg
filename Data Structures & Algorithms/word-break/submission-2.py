class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            
            if i in cache:
                return i
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return dfs(0)
