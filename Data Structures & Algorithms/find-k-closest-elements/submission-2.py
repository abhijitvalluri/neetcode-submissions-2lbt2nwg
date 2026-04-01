class Solution:
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: (abs(num - x), num))
        return sorted(arr[:k])
        
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        idx = 0
        for i in range(1, n):
            if abs(x - arr[idx]) > abs(x - arr[i]):
                idx = i
            
        res = [arr[idx]]
        l, r = idx - 1, idx + 1

        while len(res) < k:
            if l >= 0 and r < n:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
            
        return sorted(res)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(x - arr[l]) > abs(x - arr[r]):
                l += 1
            else:
                r -= 1
        
        return arr[l:r+1]