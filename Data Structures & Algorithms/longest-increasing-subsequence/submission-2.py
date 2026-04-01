class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSubsequence = -1

        def dfs(i, curLen, prevMax):
            nonlocal maxSubsequence
            if i == len(nums):
                maxSubsequence = max(maxSubsequence, curLen)
                return
            
            dfs(i + 1, curLen, prevMax)

            if nums[i] > prevMax:
                dfs(i + 1, curLen + 1, nums[i])
        
        dfs(0, 0, min(nums) - 1)
        return maxSubsequence
        