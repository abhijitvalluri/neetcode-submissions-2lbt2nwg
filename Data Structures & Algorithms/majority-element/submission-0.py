class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        majority_count = len(nums) // 2

        for num in nums:
            counts[num] += 1
            if counts[num] > majority_count:
                return num
        
        return None