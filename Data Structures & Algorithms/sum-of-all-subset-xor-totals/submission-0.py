class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(idx, curXor):
            nonlocal res
            if idx == len(nums):
                res += curXor
                return
            
            backtrack(idx + 1, curXor ^ nums[idx])
            backtrack(idx + 1, curXor)
        
        backtrack(0, 0)
        return res
        