# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        numGood = 0
        queue = deque()
        queue.append((root, -float("inf")))

        while queue:
            node, maxVal = queue.popleft()
            if not node:
                continue
            
            if node.val >= maxVal:
                numGood += 1
            
            maxVal = max(maxVal, node.val)
            queue.append((node.left, maxVal))
            queue.append((node.right, maxVal))
        
        return numGood
