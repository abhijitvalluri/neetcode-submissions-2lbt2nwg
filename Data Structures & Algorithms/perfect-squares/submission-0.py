class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}

        def dfs(num):
            if num == 0:
                return 0
            
            if num in cache:
                return cache[num]
            
            minNum = num
            for i in range(1, num):
                if i*i > num:
                    break
                minNum = min(minNum, 1 + dfs(num - i*i))
            cache[num] = minNum
            return minNum
        
        return dfs(n)
        