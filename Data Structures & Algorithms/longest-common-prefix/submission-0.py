class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for i in range(len(lcp)):
            c = lcp[i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != c:
                    return lcp[0:i]
            
        return lcp
        