class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valMap = {}

        for i in range(len(nums)):
            if nums[i] in valMap:
                diff = i - valMap[nums[i]]
                if diff <= k:
                    return True
                else:
                    valMap[nums[i]] = i
            else:
                valMap[nums[i]] = i
        
        return False
        