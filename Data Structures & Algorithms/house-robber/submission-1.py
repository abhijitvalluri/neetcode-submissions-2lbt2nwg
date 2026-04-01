class Solution:
    def rob(self, nums: List[int]) -> int:
        #cache = defaultdict(int)

        def backtrack(i, value):
            if i >= len(nums):
                return value
            
            #if i in cache:
            #    return cache[i]
            
            maxVal = max(backtrack(i + 2, value + nums[i]), backtrack(i+1, value))
            #cache[i] = maxVal
            return maxVal
        
        return backtrack(0, 0)
        