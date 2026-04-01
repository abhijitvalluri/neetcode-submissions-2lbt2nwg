# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            level = []
            newQ = []
            for node in q:
                level.append(node.val)
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            res.append(level)
            q = newQ
        
        return res

             
        