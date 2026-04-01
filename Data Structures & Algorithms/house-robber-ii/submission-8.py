class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, tookFirst):
            if i >= len(nums):
                return 0

            if i == len(nums) - 1:
                return 0 if tookFirst else nums[i]
            
            if (i, tookFirst) in cache:
                return cache[(i, tookFirst)]
            
            cache[(i, tookFirst)] = max(nums[i] + dfs(i + 2, tookFirst), dfs(i + 1, tookFirst))
            return cache[(i, tookFirst)]
        
        return max(nums[0] + dfs(2, True), dfs(1, False))
