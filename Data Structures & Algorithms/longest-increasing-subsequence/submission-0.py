class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSubsequence = -1

        def dfs(i, curLen, prevMax):
            nonlocal maxSubsequence
            if i == len(nums):
                maxSubsequence = max(maxSubsequence, curLen)
                return
            
            if nums[i] > prevMax:
                dfs(i + 1, curLen + 1, nums[i])
                dfs(i + 1, curLen, prevMax)
        
        dfs(0, 0, -float("inf"))
        return maxSubsequence
        