# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        q = [root]
        while len(q) != 0:
            res.append(q[-1].val)
            son = []
            for node in q:
                if node.left is not None:
                    son.append(node.left)
                if node.right is not None:
                    son.append(node.right)
            q = son
        return res


'''
用bfs
'''
