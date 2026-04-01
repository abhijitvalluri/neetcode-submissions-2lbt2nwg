class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tot = 2 ** len(nums)
        res = []

        for i in range(tot):
            mask = 1
            subset = []
            for num in nums:
                if mask & i:
                    subset.append(num)
                mask <<= 1
            res.append(subset)
                    
        return res
