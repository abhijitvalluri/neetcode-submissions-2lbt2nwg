class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""
        
        countT = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(countT)
        res, resLen = [0, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""