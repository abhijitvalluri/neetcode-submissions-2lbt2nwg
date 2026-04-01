class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                l, r = i + 1, len(nums) - 1
                
                while l < r:
                    threeSum = nums[i] + nums[l] + nums[r]

                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        
        return result