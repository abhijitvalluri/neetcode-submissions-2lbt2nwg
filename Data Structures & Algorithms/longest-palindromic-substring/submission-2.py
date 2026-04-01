class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        def searchPalindrome(l, r):
            nonlocal resIdx, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

        for i in range(len(s)):
            searchPalindrome(i, i)
            searchPalindrome(i, i + 1)
        
        return s[resIdx: resIdx + resLen]
