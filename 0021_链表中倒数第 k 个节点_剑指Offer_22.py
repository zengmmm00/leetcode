# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        global node
        count = self.recursion(head, k)
        return node

    def recursion(self, p, k):
        global node
        if p is None:
            return 0
        else:
            nextCount = self.recursion(p.next, k)
            thisCount = nextCount + 1
            if thisCount == k:
                node = p
            return thisCount
