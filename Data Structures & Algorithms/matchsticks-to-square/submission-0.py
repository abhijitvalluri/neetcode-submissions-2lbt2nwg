class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totLength = sum(matchsticks)
        if totLength % 4 != 0:
            return False
        
        length = totLength // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] > length:
                    continue
                
                sides[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                
                sides[j] -= matchsticks[i]
                if sides[j] == 0:
                    break
            
            return False
        
        return dfs(0)