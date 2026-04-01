class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        coins.sort()

        def dfs(target, idx):
            if target == 0:
                return 1
            
            if idx == len(coins):
                return 0
            
            if (target, idx) in cache:
                return cache[(target, idx)]
            
            numWays = dfs(target, idx + 1)
            if target >= coins[idx]:
                numWays += dfs(target - coins[idx], idx)
            
            cache[(target, idx)] = numWays
            return numWays
        
        return dfs(amount, 0)
