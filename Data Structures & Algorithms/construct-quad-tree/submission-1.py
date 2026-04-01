"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            if n == 1:
                return Node(grid[r][c], True)
            
            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf \
                and topleft.val == topright.val == bottomleft.val == bottomright.val:
                return Node(topleft.val, True)
        
            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)
        