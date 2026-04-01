class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i])

            if nums[val - 1] < 0:
                return val
            else:
                nums[val - 1] *= -1
        