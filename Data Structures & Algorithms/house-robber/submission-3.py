class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def backtrack(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(backtrack(i + 1), nums[i] + backtrack(i + 2))
            return cache[i]
        
        return backtrack(0)
        