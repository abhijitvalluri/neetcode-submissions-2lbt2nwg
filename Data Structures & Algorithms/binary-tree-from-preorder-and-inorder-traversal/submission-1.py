# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        preIdx = 0
        def dfs(l, r):
            nonlocal preIdx
            if l > r:
                return None
            
            node = TreeNode(preorder[preIdx])
            inIdx = indices[preorder[preIdx]]
            preIdx += 1
            node.left = dfs(l, inIdx - 1)
            node.right = dfs(inIdx + 1, r)

            return node
        
        return dfs(0, len(inorder) - 1)