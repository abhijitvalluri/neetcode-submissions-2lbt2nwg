class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix = suffix = 0
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix if prefix != 0 else 1)
            suffix = nums[n - 1 - i] * (suffix if suffix != 0 else 1)
            res = max(res, prefix, suffix)
        
        return res
