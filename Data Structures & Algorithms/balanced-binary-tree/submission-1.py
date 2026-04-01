# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        nextHasNone = False

        while queue:
            curHasNone = nextHasNone
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if curHasNone:
                    if node.left or node.right:
                        return False
                else:
                    if node.left:
                        queue.append(node.left)
                    else: 
                        nextHasNone = True
                    if node.right:
                        queue.append(node.right)
                    else:
                        nextHasNone = True
        return True

        