"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clonedNodes = {}
        q = deque()
        q.append(node)

        while q:
            oldNode = q.popleft()
            if oldNode.val not in clonedNodes:
                clonedNodes[oldNode.val] = Node(oldNode.val)
            newNode = clonedNodes[oldNode.val]

            for nbr in oldNode.neighbors:
                if nbr.val not in clonedNodes:
                    newNbr = Node(nbr.val)
                    clonedNodes[nbr.val] = newNbr
                    q.append(nbr)
                newNode.neighbors.append(clonedNodes[nbr.val])

        return clonedNodes[node.val]
                