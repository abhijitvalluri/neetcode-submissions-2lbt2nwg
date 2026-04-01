class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            dfs(i+1, subset)
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
        
        return res
        