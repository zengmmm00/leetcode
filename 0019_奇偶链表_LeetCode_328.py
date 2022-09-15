# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        o = odd
        e = even
        while True:
            n = e.next
            if n is None:
                break
            o.next = n
            o = n
            n = o.next
            if n is None:
                break
            e.next = n
            e = n
        o.next = even
        e.next = None
        return odd


'''
even链最后一个结点的next要设为None，否则会产生环。
'''
