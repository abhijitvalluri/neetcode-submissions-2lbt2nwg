class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(idx):
            
            if idx in cache:
                return cache[idx]
            
            length = 1
            for j in range(idx, len(nums)):
                if nums[idx] < nums[j]:
                    length = max(length, 1 + dfs(j))
            
            cache[idx] = length
            return length
        
        return max(dfs(i) for i in range(len(nums)))
