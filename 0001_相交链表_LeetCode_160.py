# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ca = self.count(headA)
        cb = self.count(headB)
        diff = cb - ca
        if diff >= 0:
            return self.getConnect(headA, headB, diff)
        else:
            return self.getConnect(headB, headA, -diff)

    def getConnect(self, headA, headB, diff):
        pb = headB
        while diff > 0:
            pb = pb.next
            diff -= 1

        pa = headA
        while pa is not None:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        return None

    def count(self, node):
        c = 0
        p = node
        while p is not None:
            c += 1
            p = p.next
        return c
