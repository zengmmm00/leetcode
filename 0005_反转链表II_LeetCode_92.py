# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        step = 1
        lnode = head

        if lnode is None or left == right:
            return head
        p1 = None
        while step < left:
            if lnode.next is None:
                return head
            p1 = lnode
            lnode = lnode.next
            step += 1

        rnode = lnode
        while step < right:
            rnode = rnode.next
            step += 1
        p2 = rnode.next

        if lnode.next != rnode:
            former = lnode
            node = former.next
            while former != rnode:
                tmp = node.next
                node.next = former
                former = node
                node = tmp
        else:
            rnode.next = lnode
        if p1 is None:
            head = rnode
        else:
            p1.next = rnode
        lnode.next = p2

        return head
