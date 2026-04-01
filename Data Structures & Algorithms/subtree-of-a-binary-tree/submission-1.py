# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            
            if not (node1 and node2) or node1.val != node2.val:
                return False
            
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if isSameTree(node, subRoot):
                return True
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        return False