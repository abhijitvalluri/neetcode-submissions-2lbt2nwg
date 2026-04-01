class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = 0

        for num in nums:
            currSum += num
            if currSum < 0:
                currSum = 0
            maxSum = max(maxSum, currSum)
        return maxSum
        