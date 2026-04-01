class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def dfs(perm, picked):
            if len(perm) == size:
                res.append(perm.copy())
                return
            
            for i in range(size):
                if not picked[i]:
                    picked[i] = True
                    perm.append(nums[i])
                    dfs(perm, picked)
                    picked[i] = False
                    perm.pop()
        
        dfs([], [False] * size)
        return res
            