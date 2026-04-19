# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node, canRob):
            if not node:
                return 0

            if (node, canRob) in cache:
                return cache[(node, canRob)]
            
            loot = dfs(node.left, True) + dfs(node.right, True)
            if canRob:
                loot = max(loot, node.val + dfs(node.left, False) + dfs(node.right, False))
            
            cache[(node, canRob)] = loot
            return loot
        
        return dfs(root, True)
