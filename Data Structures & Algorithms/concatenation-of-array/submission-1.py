class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(2):
            for num in nums:
                result.append(num)

        return result
