# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        cur = dummy
        minHeap = []
        
        for head in lists:
            if head:
                heapq.heappush(minHeap, NodeWrapper(head))
        
        while minHeap:
            node = heapq.heappop(minHeap).node
            cur.next = node
            cur = node

            if node.next:
                heapq.heappush(minHeap, NodeWrapper(node.next))
        
        return dummy.next
        