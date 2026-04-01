class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def backtrack(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            maxVal = max(backtrack(i + 1), nums[i] + backtrack(i + 2))
            cache[i] = maxVal
            return maxVal
        
        return backtrack(0)
        