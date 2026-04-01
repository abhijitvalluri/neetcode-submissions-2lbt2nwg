# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.res = None
    
    def dfs(self, node):
        if not node or self.count == 0:
            return
        self.dfs(node.left)
        self.count -= 1
        if self.count == 0:
            self.res = node.val
            return
        self.dfs(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None

        self.dfs(root)
        return self.res

        