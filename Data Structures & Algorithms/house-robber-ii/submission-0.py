class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cache = defaultdict(lambda: defaultdict(int))

        def backtrack(i, tookFirst):
            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1:
                return nums[i] if not tookFirst else 0
            
            if i in cache and tookFirst in cache[i]:
                return cache[i][tookFirst]
            
            cache[i][tookFirst] = max(backtrack(i + 1, tookFirst), nums[i] + backtrack(i + 2, tookFirst))
            return cache[i][tookFirst]
        
        return max(backtrack(1, False), nums[0] + backtrack(2, True))
