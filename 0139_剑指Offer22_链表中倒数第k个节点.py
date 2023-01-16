# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        self.res = None
        n = self.getNode(head, k)
        return self.res

    def getNode(self, node, k):
        if node is None:
            return 0
        else:
            n = self.getNode(node.next, k)
            if n + 1 == k:
                self.res = node
            return n + 1
