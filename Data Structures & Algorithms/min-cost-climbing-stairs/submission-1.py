class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def calcMinCost(floor):
            if floor >= n:
                return 0
            elif floor in cache:
                return cache[floor]
            
            cache[floor] = cost[floor] + min(calcMinCost(floor + 1), calcMinCost(floor + 2))
            return cache[floor]

        return min(calcMinCost(0), calcMinCost(1))
