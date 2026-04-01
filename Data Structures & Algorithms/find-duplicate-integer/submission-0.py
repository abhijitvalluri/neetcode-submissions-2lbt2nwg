class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                return i + 1
            
            if nums[nums[i] - 1] < 0:
                return nums[i]
            else:
                nums[nums[i] - 1] *= -1
        