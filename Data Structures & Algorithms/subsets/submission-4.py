class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tot = 2 ** len(nums)

        for i in range(tot):
            mask = 1
            subset = []
            for num in nums:
                if mask & i:
                    subset.append(num)
                mask <<= 1
            
            res.append(subset)
        
        return res
        