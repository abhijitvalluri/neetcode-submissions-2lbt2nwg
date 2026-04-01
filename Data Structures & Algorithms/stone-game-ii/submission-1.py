class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        m = 1

        def dfs(alice, l, m):
            if l >= len(piles):
                return 0
            
            if (alice, l, m) in cache:
                return cache[(alice, l, m)]
            
            if not alice:
                if 2*m >= len(piles) - l + 1:
                    cache[(alice, l, m)] = 0
                else:
                    res = float("inf")
                    for i in range(1, 2*m + 1):
                        res = min(res, dfs(not alice, l + i, max(m, i)))
                    cache[(alice, l, m)] = res
            else:
                if 2*m >= len(piles) - l + 1:
                    cache[(alice, l, m)] = sum(piles[l:])
                else:
                    res, val = 0, 0
                    for i in range(2*m):
                        if l + i == len(piles):
                            break
                        val += piles[l + i]
                        res = max(res, val + dfs(not alice, l + i + 1, max(m, i + 1)))
                    cache[(alice, l, m)] = res
            return cache[(alice, l, m)]
        
        return dfs(True, 0, 1)
