# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        
        newHead = None
        nextGroup = head
        prevGroup = None
        cur = head
        count = 0

        while cur:
            temp_next = cur.next
            count += 1
            if count == k:
                count = 0
                if not newHead:
                    newHead = cur
                prev = None
                node = nextGroup
                while node != temp_next:
                    temp = node.next
                    node.next = prev
                    prev = node
                    node = temp
                if prevGroup:
                    prevGroup.next = cur
                prevGroup = nextGroup
                nextGroup = temp_next
            
            cur = temp_next
        
        if count and prevGroup:
            prevGroup.next = nextGroup

        return newHead if newHead else head
    