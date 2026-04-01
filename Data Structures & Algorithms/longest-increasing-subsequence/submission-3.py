class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = defaultdict(lambda: defaultdict(int))

        def dfs(curIdx, prevIdx):
            if curIdx == len(nums):
                return 0
            
            if curIdx in cache and prevIdx in cache[curIdx]:
                return cache[curIdx][prevIdx]

            longestSeq = dfs(curIdx + 1, prevIdx)

            if prevIdx == -1 or nums[prevIdx] < nums[curIdx]:
                longestSeq = max(longestSeq, 1 + dfs(curIdx + 1, curIdx))            
            
            cache[curIdx][prevIdx] = longestSeq
            return longestSeq
        
        return dfs(0, -1)
        