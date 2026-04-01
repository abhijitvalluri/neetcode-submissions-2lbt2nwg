class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        processed = set()

        def sumSqrDigits(num):
            tot = 0
            while num:
                d = num % 10
                num //= 10
                tot += d * d
            
            return tot

        num = n
        while num not in processed:
            processed.add(num)
            num = sumSqrDigits(num)
        
        return num == 1
        