# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root, -float('inf')))

        while q:
            node, maxVal = q.popleft()
            if not node:
                continue
            res += 1 if node.val >= maxVal else 0
            
            maxVal = max(node.val, maxVal)
            q.append((node.left, maxVal))
            q.append((node.right, maxVal))
            
        return res

    def goodNodesDfs(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)
