class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            ad = 0 if i < 0 else a[i] == "1"
            bd = 0 if j < 0 else b[j] == "1"

            total = ad + bd + carry
            carry = total // 2
            res.append(str(total % 2))
            i -= 1
            j -= 1

        res.reverse()
        return "".join(res)
        