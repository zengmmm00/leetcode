# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        n = head
        while n is not None and n.next is not None:
            if n.next.val == val:
                p = n.next.next
                n.next = p
            else:
                n = n.next
        return head


'''
删除元素后指针不用移到下一个。
'''
