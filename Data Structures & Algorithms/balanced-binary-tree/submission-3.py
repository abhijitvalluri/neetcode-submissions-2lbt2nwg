# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            
            lBal, lHeight = dfs(node.left)
            rBal, rHeight = dfs(node.right)
            balanced = lBal and rBal and abs(lHeight - rHeight) <= 1
            return [balanced, 1 + max(lHeight, rHeight)]
        
        return dfs(root)[0]