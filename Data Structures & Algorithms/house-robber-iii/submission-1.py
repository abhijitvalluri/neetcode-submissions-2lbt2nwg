# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node): # Return value is (value if robbing this node, value if skipped)
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # If I rob this node, skip children, so take array elem 1.
            rob = node.val + left[1] + right[1]

            # If I skip this node, then take the best outcome for left and best for right
            skip = max(left) + max(right)

            return (rob, skip)
        
        return max(dfs(root)) # Return the best outcome between starting with robbing root or skipping root
