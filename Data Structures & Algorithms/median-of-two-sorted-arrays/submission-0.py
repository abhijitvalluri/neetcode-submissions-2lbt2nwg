class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l1, r1 = 0, len(nums1) - 1
        mid1, mid2 = 0, 0

        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            mid1 = (l1 + r1) // 2
            mid2 = half - mid1  - 2

            left1 = float("-inf") if mid1 < 0 else nums1[mid1]
            right1 = float("inf") if mid1 >= len(nums1) - 1 else nums1[mid1 + 1]

            left2 = float("-inf") if mid2 < 0 else nums2[mid2]
            right2 = float("inf") if mid2 >= len(nums2) - 1 else nums2[mid2 + 1]

            if left1 <= right2 and left2 <= right1:
                if total % 2 != 0:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2
            elif left1 > right2:
                r1 = mid1 - 1
            else:
                l1 = mid1 + 1
            