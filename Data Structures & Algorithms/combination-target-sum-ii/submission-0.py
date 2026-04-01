class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                num = candidates[j]
                if total + num > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                cur.append(num)
                dfs(j + 1, cur, total + num)
                cur.pop()
        
        dfs(0, [], 0)
        return res
