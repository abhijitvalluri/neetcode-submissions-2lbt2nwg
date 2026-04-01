# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        n1, n2 = l1, l2

        carry = 0
        prev, head = None, None
        while n1 and n2:
            total = n1.val + n2.val + carry
            node = None
            if total > 9:
                val = total - 10
                carry = 1
                node = ListNode(val)
            else:
                carry = 0
                node = ListNode(total)

            if not prev:
                prev = node
                head = node
            else:
                prev.next = node
                prev = node
            n1, n2 = n1.next, n2.next
        
        if n1:
            n1.val += carry
            prev.next = n1
        elif n2:
            n2.val += carry
            prev.next = n2
        elif carry:
            node = ListNode(carry)
            prev.next = node
        
        return head
