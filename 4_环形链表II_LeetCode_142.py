# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return None
        if head.next.next == head:
            return head
        fast = head.next
        slow = head
        while fast is not None and slow is not None and fast.next is not None and fast.next.next is not None:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                p1 = head
                p2 = fast.next
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None

'''
如果头结点有存数据，从头结点出发一个指针p1，从相遇节点也出发一个指针p2。p1走一步到头结点，p2走一步到相遇结点的下一个结点。
在判断node.next.next是否为None之前，要判断node.next是否为None。
'''