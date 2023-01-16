# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        head = ListNode()
        p = head
        while True:
            if a is not None and b is not None:
                if a.val < b.val:
                    p.next = a
                    a = a.next
                else:
                    p.next = b
                    b = b.next
            elif a is not None:
                p.next = a
                a = a.next
            elif b is not None:
                p.next = b
                b = b.next
            else:
                break
            p = p.next
        return head.next
