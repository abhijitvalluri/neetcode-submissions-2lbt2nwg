class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            ad = 0 if i < 0 else a[i] == "1"
            bd = 0 if j < 0 else b[j] == "1"

            total = ad + bd + carry

            if total > 1:
                total = ad ^ bd ^ carry
                carry = 1
            else:
                carry = 0
            res.append(str(total))
            i -= 1
            j -= 1
        
        if carry:
            res.append(str(carry))

        res.reverse()
        return "".join(res)
        