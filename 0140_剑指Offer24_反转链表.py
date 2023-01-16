# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = head
        a = p
        b = p.next
        c = p.next.next
        while True:
            b.next = a

            if c is None:
                break
            a = b
            b = c
            c = c.next
        head.next = None
        return b
