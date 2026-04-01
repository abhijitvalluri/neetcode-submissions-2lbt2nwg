class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        majority = len(nums) // 3
        result = []

        for num in nums:
            counts[num] += 1

        for num in counts:
            if counts[num] > majority:
                result.append(num)
        
        return result
        