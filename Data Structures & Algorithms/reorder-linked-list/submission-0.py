# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        front, back = head, prev
        while back:
            temp1, temp2 = front.next, back.next
            front.next = back
            back.next = temp1
            front, back = temp1, temp2
