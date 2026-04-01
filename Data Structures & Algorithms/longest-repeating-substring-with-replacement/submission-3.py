class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = l = res = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1
            maxF = max(maxF, counts[s[r]])

            while (r - l + 1) - maxF > k:
                # length of current window - max Frequency > k
                # So, current window is invalid, as it is too big, reduce size
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
