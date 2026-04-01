class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            if carry == 0:
                return digits
            d = digits[i] + carry
            if d < 10:
                carry = 0
                digits[i] = d
            else:
                digits[i] = 0
        
        if carry:
            digits.insert(0, 1)
        return digits
        