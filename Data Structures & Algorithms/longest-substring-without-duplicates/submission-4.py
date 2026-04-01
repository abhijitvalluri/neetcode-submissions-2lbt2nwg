class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        positions = {}
        start = 0
        maxLen = 0

        for i in range(len(s) - 1):
            if s[i] in positions:
                prevIdx = positions[s[i]]
                maxLen = max(maxLen, i - start)
                start = prevIdx + 1
            positions[s[i]] = i

        if s[-1] in positions:
            maxLen = max(maxLen, len(s) - 1 - start)
        else:
            maxLen = max(maxLen, len(s) - start)

        return maxLen
