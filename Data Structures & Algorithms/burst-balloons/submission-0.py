class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            maxCoins = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                maxCoins = max(maxCoins, coins)
            cache[(l, r)] = maxCoins
            return maxCoins

        return dfs(1, len(nums) - 2)