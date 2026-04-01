# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if self.isSameTree(node, subRoot):
                return True
            else:
                if node:
                    q.append(node.left)
                    q.append(node.right)
                
        return False
