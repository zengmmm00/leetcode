# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        node = head
        while node is not None:
            if p1 is None:
                node.next = p2
                return head
            if p2 is None:
                node.next = p1
                return head

            if p1.val < p2.val:
                node.next = p1
                p1 = p1.next
            else:
                node.next = p2
                p2 = p2.next
            node = node.next
        return head
