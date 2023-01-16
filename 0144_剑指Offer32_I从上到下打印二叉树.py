# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q = queue.Queue()
        if root is None:
            return []
        q.put(root)
        res = []
        while q.empty() is False:
            node = q.get()
            res.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return res
