# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
MAX = 10001


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        f = True
        for x in lists:
            if x is not None:
                f = False
                break
        if f:
            return None

        p = [x for x in lists]
        value = []
        for i in range(len(lists)):
            if lists[i] is None:
                value.append(MAX)
            else:
                value.append(lists[i].val)
        minI = value.index(min(value))
        minV = value[minI]
        res = []
        while minV != MAX:
            res.append(p[minI])
            p[minI] = p[minI].next
            if p[minI] is None:
                value[minI] = MAX
            else:
                value[minI] = p[minI].val

            minI = value.index(min(value))
            minV = value[minI]

        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        if len(res) != 0:
            res[-1].next = None
            return res[0]
        return None
