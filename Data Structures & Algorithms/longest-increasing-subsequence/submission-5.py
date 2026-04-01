class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(currIdx, prevIdx):
            if currIdx == len(nums):
                return 0
            
            if (currIdx, prevIdx) in cache:
                return cache[(currIdx, prevIdx)]
            
            length = 0
            if prevIdx == -1 or nums[currIdx] > nums[prevIdx]:
                length = 1 + dfs(currIdx + 1, currIdx)
            
            length = max(length, dfs(currIdx + 1, prevIdx))
            cache[(currIdx, prevIdx)] = length
            return length
        
        return dfs(0, -1)
