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
        q = [root]
        res = []
        odd = True
        while len(q) != 0:
            tmp = [node.val for node in q]
            if odd is False:
                tmp = tmp[::-1]
                odd = True
            else:
                odd = False
            res.append(tmp)
            nq = []
            for node in q:
                if node.left is not None:
                    nq.append(node.left)
                if node.right is not None:
                    nq.append(node.right)
            q = nq
        return res
