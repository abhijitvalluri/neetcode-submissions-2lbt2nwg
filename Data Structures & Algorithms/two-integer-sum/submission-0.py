class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_locs = {}

        for i, num in enumerate(nums):
            if num not in num_locs:
                num_locs[num] = []
            num_locs[num].append(i)
        
        for i, num in enumerate(nums):
            remain = target - num
            if remain in num_locs:
                if remain != num:
                    return [i, num_locs[remain][0]]
                elif len(num_locs[remain]) > 1:
                    return [i, num_locs[remain][1]]
        
        return []
        