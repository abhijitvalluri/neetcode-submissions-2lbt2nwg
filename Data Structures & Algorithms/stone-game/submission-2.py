class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            isAliceTurn = (r - l + 1) % 2 == 0
            if isAliceTurn: # We maximise the value
                cache[(l, r)] = max(piles[l] + dfs(l + 1, r), piles[r] + dfs(l, r - 1))
            else: # Bob will maximise his value, so he minimises Alice's value
                cache[(l, r)] = min(dfs(l + 1, r), dfs(l, r - 1))
            
            return cache[(l, r)]
        
        aliceScore = dfs(0, len(piles) - 1)
        totalStones = sum(piles)
        return aliceScore > totalStones - aliceScore
