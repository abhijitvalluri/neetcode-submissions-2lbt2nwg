# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def search(self, l, r) -> int:
        mid = (l + r) // 2
        val = guess(mid)
        if val == 0:
            return mid
        elif val == -1:
            return self.search(l, mid-1)
        else:
            return self.search(mid+1, r)

    def guessNumber(self, n: int) -> int:
        return self.search(1, n)
        