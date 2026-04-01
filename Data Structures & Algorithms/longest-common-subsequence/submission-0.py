class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = defaultdict(int)

        def backtrack(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + backtrack(i + 1, j + 1)
            else:
                cache[(i, j)] = max(backtrack(i + 1, j), backtrack(i, j + 1))
            
            return cache[(i, j)]
        
        return backtrack(0, 0)
