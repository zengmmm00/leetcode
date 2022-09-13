# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        nh = ListNode(-1, head)
        i = 1
        p = head
        a = nh
        while p is not None:
            if i != k:
                stack.append(p)
                p = p.next
                i += 1
            else:
                stack.append(p)
                b = p.next
                if len(stack) != 0:
                    for j in range(len(stack) - 1, 0, -1):
                        stack[j].next = stack[j - 1]

                    a.next = stack[-1]
                    stack[0].next = b
                    p = stack[0]
                a = p
                stack.clear()
                p = p.next
                i = 1
        return nh.next
