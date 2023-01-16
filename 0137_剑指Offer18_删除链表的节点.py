# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        if val == head.val:
            return head.next
        p = head
        while p.next is not None and p.next.val != val:
            p = p.next
        if p.next is None:
            return head
        tmp = p.next.next
        p.next = tmp
        return head
