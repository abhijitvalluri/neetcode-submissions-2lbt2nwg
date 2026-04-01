class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        uniqueNums = set(nums)
        l, r, size = 0, 1, len(nums)

        res = []

        while r < size - 1:
            while r < size - 1 and nums[l] == nums[r] and nums[r] == nums[r + 1]:
                r += 1
            total = nums[l] + nums[r]
            if -total > nums[r] and -total in uniqueNums:
                res.append([nums[l], nums[r], -total])
            l, r = r, r + 1
        
        return res
