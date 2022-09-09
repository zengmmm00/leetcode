"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = dict()
        p = head
        c = 0
        l = []

        while p is not None:
            n = Node(p.val)
            l.append(n)
            d[p] = c
            c += 1
            p = p.next

        p = head
        for i in range(len(l)):
            if i + 1 != len(l):
                l[i].next = l[i + 1]
            if p.random is not None:
                l[i].random = l[d[p.random]]
            p = p.next

        if len(l) == 0:
            return None

        return l[0]


'''
return l[0]前要判断l是否为空。
用字典前要判断key是否为None。
'''
