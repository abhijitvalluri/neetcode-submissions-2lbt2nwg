class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        positions = {}
        start = 0
        maxLen = 1

        for i in range(len(s)):
            if s[i] in positions:
                prevIdx = positions[s[i]]
                maxLen = max(maxLen, i - start)
                start = prevIdx + 1
            positions[s[i]] = i

        return maxLen
