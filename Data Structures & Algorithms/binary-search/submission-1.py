class Solution:
    def binSrch(self, nums, target, l, r) -> int:
        if l > r:
            return - 1
        
        mid = (r + l - 1) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binSrch(nums, target, mid+1, r)
        else:
            return self.binSrch(nums, target, l, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        return self.binSrch(nums, target, 0, len(nums)-1)
        