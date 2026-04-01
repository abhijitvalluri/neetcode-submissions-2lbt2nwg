class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                b = nums[j]
                rem = target - a - b
                l, r = j + 1, len(nums) - 1

                while l < r:
                    twoSum = nums[l] + nums[r]
                    if twoSum > rem:
                        r -= 1
                    elif twoSum < rem:
                        l += 1
                    else:
                        result.append([a, b, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        
        return result
