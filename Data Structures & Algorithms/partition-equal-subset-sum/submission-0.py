class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        cache = defaultdict(lambda: defaultdict(bool))

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            
            if target < 0:
                return False

            if not (i in cache and target in cache[i]):
                cache[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return cache[i][target]
        
        return dfs(0, sum(nums) // 2)
