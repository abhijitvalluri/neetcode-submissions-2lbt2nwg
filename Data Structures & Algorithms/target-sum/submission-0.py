class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(idx, total):
            if total == target and idx == len(nums):
                return 1
            if idx == len(nums):
                return 0

            if (idx, total) in cache:
                return cache[(idx, total)]
            
            cache[(idx, total)] = dfs(idx + 1, total + nums[idx]) + dfs(idx + 1, total - nums[idx])
            return cache[(idx, total)]
        
        return dfs(0, 0)