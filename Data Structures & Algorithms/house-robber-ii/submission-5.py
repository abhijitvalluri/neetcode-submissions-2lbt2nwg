class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def backtrack(i, tookFirst):
            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1:
                return nums[i] if not tookFirst else 0
            
            if (i, tookFirst) in cache:
                return cache[(i, tookFirst)]
            
            cache[(i, tookFirst)] = max(nums[i] + backtrack(i + 2, tookFirst), backtrack(i + 1, tookFirst))
            return cache[(i, tookFirst)]
        
        return max(nums[0] + backtrack(2, True), backtrack(1, False))
