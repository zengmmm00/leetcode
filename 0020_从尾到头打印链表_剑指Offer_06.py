# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        self.recursion(head, result)
        return result

    def recursion(self, p, result):
        if p is None:
            return
        else:
            self.recursion(p.next, result)
            result.append(p.val)
            return
