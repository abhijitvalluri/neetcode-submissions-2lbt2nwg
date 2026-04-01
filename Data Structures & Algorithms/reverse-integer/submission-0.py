class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1
        minVal = -2 ** 31
        maxVal = 2 ** 31 - 1
        x = abs(x)
        res = 0

        while x:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        res *= sign
        if minVal <= res <= maxVal:
            return res
        
        return 0
