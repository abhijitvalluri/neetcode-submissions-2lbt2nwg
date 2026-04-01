class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(total):
            if total == 0:
                return 1

            if total in cache:
                return cache[total]

            res = 0
            for i in range(len(nums)):
                if total >= nums[i]:
                    res += dfs(total - nums[i])
            cache[total] = res
            return res
        
        return dfs(target)