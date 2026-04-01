# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node):
        if not node:
            return [True, 0]
        leftBal, left = self.height(node.left)
        rightBal, right = self.height(node.right)
        if not leftBal or not rightBal:
            return [False, 0]
        if abs(left - right) > 1:
            return [False, 0]
        else:
            return [True, 1 + max(left, right)]
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal, height = self.height(root)
        return bal
        