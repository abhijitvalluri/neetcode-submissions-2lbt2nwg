class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        def backtrack(idx):
            if idx == len(s):
                return True
            
            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] in words:
                    if backtrack(i):
                        return True
            
            return False
        
        return backtrack(0)
