class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        size = len(nums)

        def dfs(perm, picked):
            if len(perm) == size:
                res.append(perm.copy())
                return
            
            for i in range(size):
                if picked[i] or (i > 0 and nums[i] == nums[i - 1] and not picked[i - 1]):
                    continue
                picked[i] = True
                perm.append(nums[i])
                dfs(perm, picked)
                picked[i] = False
                perm.pop()
            
        dfs([], [False] * size)
        return res
