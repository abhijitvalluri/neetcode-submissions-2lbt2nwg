class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False
        x, y, z = target

        for i, j, k in triplets:
            a |= (i == x and j <= y and k <= z)
            b |= (i <= x and j == y and k <= z)
            c |= (i <= x and j <= y and k == z)
            if a and b and c:
                return True
        
        return False
        