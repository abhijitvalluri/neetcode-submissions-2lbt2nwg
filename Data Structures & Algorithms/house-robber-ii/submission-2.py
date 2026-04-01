class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for i in range(len(nums) - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1, rob2 = rob2, temp
        
        maxTakeFirst = rob2

        rob1 = rob2 = 0
        for i in range(1, len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1, rob2 = rob2, temp

        return max(maxTakeFirst, rob2)          
