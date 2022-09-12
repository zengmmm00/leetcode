# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.inverse(head, None)

    def inverse(self, node, former):
        if node is None:
            return former

        latter = node.next
        node.next = former
        return self.inverse(latter, node)
