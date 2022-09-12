# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        pl = less
        pg = greater
        while head is not None:
            if head.val < x:
                pl.next = head
                pl = pl.next
            else:
                pg.next = head
                pg = pg.next
            head = head.next
        pg.next = None
        pl.next = greater.next
        return less.next


'''
node的next要设为None，防止出现环。
'''
