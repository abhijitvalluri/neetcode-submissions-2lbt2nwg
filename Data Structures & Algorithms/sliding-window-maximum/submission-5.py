class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        leftMax = [0] * size
        rightMax = [0] * size

        leftMax[0] = nums[0]
        rightMax[size - 1] = nums[size - 1]

        for i in range(1, size):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i-1], nums[i])
            
            if (size - 1 - i) % k == 0:
                rightMax[size - 1 - i] = nums[size - 1 - i]
            else:
                rightMax[size - 1 - i] = max(rightMax[size - i], nums[size - 1 - i])

        res = [0] * (size - k + 1)
        for i in range(size - k + 1):
            res[i] = max(rightMax[i], leftMax[i + k - 1])

        return res        