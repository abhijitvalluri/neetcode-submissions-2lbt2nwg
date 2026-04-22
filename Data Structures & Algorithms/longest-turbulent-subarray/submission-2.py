class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize = currSize = 0
        sign = -1

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                currSize = currSize + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                currSize = currSize + 1 if sign == 1 else 1
                sign = 0
            else:
                currSize = 0
                sign = -1
        
            maxSize = max(maxSize, currSize)
        
        return maxSize + 1
