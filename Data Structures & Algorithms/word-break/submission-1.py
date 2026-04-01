class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}

        def backtrack(idx):
            if idx == len(s):
                return True

            if idx in cache:
                return cache[idx]
            
            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] in words:
                    if backtrack(i):
                        cache[idx] = True
                        return True
            
            cache[idx] = False
            return False
        
        return backtrack(0)
