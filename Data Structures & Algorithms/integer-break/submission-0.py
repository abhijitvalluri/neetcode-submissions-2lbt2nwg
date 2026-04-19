class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {1: 1}

        def dfs(num):
            if num in cache:
                return cache[num]
            
            best = num if num != n else 0
            for i in range(1, num):
                best = max(best, dfs(i) * dfs(num - i))
            cache[num] = best
            return best
        
        return dfs(n)
