# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None or A is None:
            return False
        q = queue.Queue()
        q.put(A)
        while q.empty() is False:
            node = q.get()
            if node is None:
                continue
            if self.getList(node, B):
                return True
            else:
                q.put(node.left)
                q.put(node.right)
        return False

    def getList(self, a, b):
        if b is None:
            return True
        if a is None:
            return False
        if b.val != a.val:
            return False
        left = self.getList(a.left, b.left)
        right = self.getList(a.right, b.right)
        return left and right
