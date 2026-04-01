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
        
        if not n1 and not n2:
            if carry:
                prev.next = ListNode(carry)
        else:
            n = n1 if n1 else n2
            while n:
                total = n.val + carry
                if total > 9:
                    carry = 1
                    val = total - 10
                    node = ListNode(val)
                    prev.next = node
                    prev = node
                    n = n.next
                else:
                    node = ListNode(total)
                    prev.next = node
                    node.next = n.next
                    break
            
        if carry:
            prev.next = ListNode(carry)
        return head
