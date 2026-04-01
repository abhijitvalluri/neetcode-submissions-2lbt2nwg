class Solution:
    def climbStairs(self, n: int) -> int:
        ways_from = {}

        def stepsFrom(step):
            if step > n:
                return 0
            elif step == n - 1 or step == n:
                return 1
            elif step in ways_from:
                return ways_from[step]
            else:
                ways_from[step] = stepsFrom(step + 1) + stepsFrom(step + 2)
                return ways_from[step]

        return stepsFrom(0)
        