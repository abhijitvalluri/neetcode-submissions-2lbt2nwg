class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []

        while i < len(word1) and j < len(word2):
            if i == j:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1
        
        while i < len(word1):
            result.append(word1[i])
            i += 1
        
        while j < len(word2):
            result.append(word2[j])
            j += 1

        return ''.join(result)
        