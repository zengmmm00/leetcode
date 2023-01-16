# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        la = self.count(headA)
        lb = self.count(headB)
        if la < lb:
            return self.getVal(headA, headB, la, lb)
        else:
            return self.getVal(headB, headA, lb, la)

    def getVal(self, headA, headB, la, lb):
        diff = lb - la
        pa = headA
        pb = headB
        for i in range(diff):
            pb = pb.next
        while pa is not None:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        return None

    def count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count(node.next)
