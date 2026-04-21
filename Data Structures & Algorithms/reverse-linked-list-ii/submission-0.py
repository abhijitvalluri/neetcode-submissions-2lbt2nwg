# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left >= right:
            return head
        
        if not head:
            return None

        before = first = last = end = None
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while right >= 0 and curr.next:
            left -= 1
            if left == 0:
                before, first = curr, curr.next
            if right == 0:
                last, end = curr, curr.next
            right -= 1
            curr = curr.next
        
        last.next = None
        reversedSubList = self.reverseList(first)
        before.next = reversedSubList
        first.next = end

        return dummy.next
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        
