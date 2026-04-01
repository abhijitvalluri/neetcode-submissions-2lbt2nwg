# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: int, leftVal: float, rightVal: float) -> bool:
        if not node:
            return True
        
        if not (leftVal < node.val < rightVal):
            return False
        
        return self.dfs(node.left, leftVal, node.val) and self.dfs(node.right, node.val, rightVal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))   
    