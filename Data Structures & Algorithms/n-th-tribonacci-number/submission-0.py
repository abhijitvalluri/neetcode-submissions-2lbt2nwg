class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        first, second, third = 0, 1, 1
        cur = 2

        while cur < n:
            temp = first + second + third
            first, second, third = second, third, temp
            cur += 1
        
        return third
        