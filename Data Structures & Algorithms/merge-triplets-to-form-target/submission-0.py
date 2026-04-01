class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        x, y, z = target

        for i, j, k in triplets:
            if i == x and j == y and k == z:
                return True
            elif i <=x and j <= y and k <= z:
                if i == x:
                    good.add(0)
                if j == y:
                    good.add(1)
                if k == z:
                    good.add(2)
            
        return len(good) == 3

        