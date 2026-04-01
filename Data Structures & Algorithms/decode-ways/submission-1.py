class Solution:
    def numDecodings(self, s: str) -> int:
        cache = defaultdict(int)

        def dfs(i):
            if i == len(s):
                return 1
            
            if i in cache:
                return cache[i]
            
            numWays = 0
            if s[i] in "123456789":
                numWays += dfs(i+1)
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                numWays += dfs(i+2)
            
            cache[i] = numWays
            return numWays
        
        return dfs(0)
