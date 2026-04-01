class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def ways(num):
            if num == 0:
                return 1
            if num < 0:
                return 0
            
            if num in cache:
                return cache[num]
            
            cache[num] = ways(num - 1) + ways(num - 2)
            return cache[num]
        
        return ways(n)
        