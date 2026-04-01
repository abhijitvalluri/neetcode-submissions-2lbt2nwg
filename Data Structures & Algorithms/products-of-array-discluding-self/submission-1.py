class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
                if zeros > 1:
                    return [0] * len(nums)
        
        result = []
        for num in nums:
            if zeros:
                val = 0 if num else prod
                result.append(val)
            else:
                result.append(prod//num)
        
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
        