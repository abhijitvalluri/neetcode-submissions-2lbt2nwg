class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(pos):
            if pos >= len(nums):
                return 0
            
            if pos in cache:
                return cache[pos]
            
            cache[pos] = max(nums[pos] + dfs(pos + 2), dfs(pos + 1))
            return cache[pos]
        
        return dfs(0)
        