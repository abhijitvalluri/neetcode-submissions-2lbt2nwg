class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(combination, m):
            if len(combination) == k:
                res.append(combination.copy())
                # return
            
            for i in range(m, n + 1):
                combination.append(i)
                dfs(combination, i + 1)
                combination.pop()
        
        dfs([], 1)
        return res
