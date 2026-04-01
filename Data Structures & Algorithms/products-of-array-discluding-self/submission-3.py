class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        prevProd = 1
        for i in range(len(nums) - 2, -1, -1):
            result[i] *= prevProd * nums[i + 1]
            prevProd *= nums[i + 1]
        
        return result