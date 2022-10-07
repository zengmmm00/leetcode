# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while len(q) != 0:
            son = []
            for node in q:
                if node.left is not None:
                    son.append(node.left)
                if node.right is not None:
                    son.append(node.right)
            if len(son) == 0:
                return q[0].val
            else:
                q = son
