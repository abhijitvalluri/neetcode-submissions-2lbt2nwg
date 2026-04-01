# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")
        if val[0] == "N":
            return None
        
        root = TreeNode(int(val[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if val[i] != "N":
                node.left = TreeNode(int(val[i]))
                queue.append(node.left)
            if val[i+1] != "N":
                node.right = TreeNode(int(val[i+1]))
                queue.append(node.right)
            i += 2
        
        return root
