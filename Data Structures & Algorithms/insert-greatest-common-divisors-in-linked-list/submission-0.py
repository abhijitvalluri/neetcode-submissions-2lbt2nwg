# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        first, second = head, head.next

        while first and second:
            g = math.gcd(first.val, second.val)
            node = ListNode(g, second)
            first.next = node
            first, second = second, second.next
        
        return head