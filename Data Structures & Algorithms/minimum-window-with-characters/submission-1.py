class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        countT = Counter(t)
        window = defaultdict(int)
        res = [0, -1]
        resLen = float("inf")
        have = 0
        need = len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                # We have enough of character c in the window
                have += 1
            
            while have == need:
                # Current window is a suitable solution
                if (r - l + 1) < resLen:
                    # This is a smaller window than previous candidate
                    resLen = r - l + 1
                    res = [l, r]
                
                # Try to reduce size and see if acceptable
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # No longer have enough of s[l] in reduced window
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
