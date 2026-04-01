class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        longestSeq = 0
        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                length = 0
                while num + length in uniqueNums:
                    length += 1
                longestSeq = max(longestSeq, length)
        
        return longestSeq
        