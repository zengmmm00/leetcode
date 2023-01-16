# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = []
        q.append(root)
        res = []
        while len(q) != 0:
            res.append([node.val for node in q])
            nq = []
            for node in q:
                if node.left is not None:
                    nq.append(node.left)
                if node.right is not None:
                    nq.append(node.right)
            q = nq
        return res
