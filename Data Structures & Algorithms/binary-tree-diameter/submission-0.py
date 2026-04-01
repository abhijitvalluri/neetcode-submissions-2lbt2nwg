# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dia = 0
    
    def dfs(self, node) -> int:
        if not node:
            return 0
        
        leftHeight = self.dfs(node.left)
        rightHeight = self.dfs(node.right)
        self.dia = max(self.dia, leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.dia
        