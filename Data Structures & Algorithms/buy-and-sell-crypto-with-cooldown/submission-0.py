class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, val):
            if i >= len(prices):
                return 0
            
            if (i, val) in cache:
                return cache[(i, val)]

            if val == -1:
                cache[(i, val)] = max(dfs(i + 1, prices[i]), dfs(i + 1, val))
            else:
                cache[(i, val)] = max(prices[i] - val + dfs(i + 2, -1), dfs(i + 1, val))
            
            return cache[(i, val)]
        
        return dfs(0, -1)
