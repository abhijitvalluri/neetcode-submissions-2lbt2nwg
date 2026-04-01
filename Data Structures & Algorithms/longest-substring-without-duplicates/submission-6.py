class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l, r = 0, 0
        maxWindow = 0

        for r in range(len(s)):
            if s[r] not in window:
                maxWindow = max(maxWindow, r - l + 1)
            else:
                newL = window[s[r]] + 1
                while l < newL:
                    del window[s[l]]
                    l += 1
            window[s[r]] = r
        return maxWindow
        