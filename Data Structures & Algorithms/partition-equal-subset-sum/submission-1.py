class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        cache = {}
        def dfs(i, target):
            if target == 0:
                return True

            if i == len(nums):
                return target == 0
    
            if (i, target) in cache:
                return cache[(i, target)]
            
            res = dfs(i+1, target)
            if nums[i] <= target:
                res = res or dfs(i+1, target - nums[i])
            
            cache[(i, target)] = res
            return res

        return dfs(0, sum(nums) // 2)
