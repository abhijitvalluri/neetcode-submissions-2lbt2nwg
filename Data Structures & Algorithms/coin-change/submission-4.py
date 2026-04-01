class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {coin: 1 for coin in coins}

        def dfs(val):
            if val == 0:
                return 0
            
            if val in cache:
                return cache[val]

            numCoins = float("inf")
            for coin in coins:
                if val >= coin:
                    numCoins = min(numCoins, 1 + dfs(val - coin))
            
            cache[val] = numCoins
            return numCoins
        
        res = dfs(amount)
        return res if res != float("inf") else -1
        