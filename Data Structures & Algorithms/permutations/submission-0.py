class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perm.append(nums[i])
                    backtrack(perm, pick)
                    perm.pop()
                    pick[i] = False
        
        backtrack([], [False] * len(nums))
        return res
