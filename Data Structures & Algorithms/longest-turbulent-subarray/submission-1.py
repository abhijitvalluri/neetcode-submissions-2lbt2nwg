class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        maxSize = currSize = 0
        nextOrder = None

        for i in range(len(arr) - 1):
            if not nextOrder:
                if arr[i] == arr[i + 1]:
                    continue
                nextOrder = -1 if arr[i] < arr[i + 1] else 1
                currSize = 2
            else:
                if nextOrder * (arr[i] - arr[i + 1]) < 0:
                    currSize += 1
                    nextOrder *= -1 
                elif nextOrder * (arr[i] - arr[i + 1]) > 0:
                    maxSize = max(maxSize, currSize)
                    currSize = 2
                else:
                    maxSize = max(maxSize, currSize)
                    currSize = 0
                    nextOrder = None
        
        return max(maxSize, currSize)
