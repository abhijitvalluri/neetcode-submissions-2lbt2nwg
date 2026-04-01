class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = defaultdict(int)
        
        for coin in coins:
            cache[coin] = 1
        
        def dfs(target):
            if target == 0:
                return 0
            
            if target in cache:
                return cache[target]

            minCoins = float("inf")
            for coin in coins:
                if target >= coin:
                    minCoins = min(minCoins, 1 + dfs(target - coin))
            cache[target] = minCoins
            return minCoins
        
        res = dfs(amount)
        return res if res != float("inf") else -1
        