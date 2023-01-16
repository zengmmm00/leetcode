# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        arr = []
        p = head
        while p is not None:
            arr.append(p.val)
            p = p.next
        return arr[::-1]
