# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return
        q = [root]
        left = True
        while len(q) != 0:
            val = []
            son = []
            for node in q:
                if node is not None:
                    val.append(node.val)
                    son.append(node.left)
                    son.append(node.right)
            if len(val) != 0:
                if left:
                    res.append(val)
                    left = False
                else:
                    val = val[::-1]
                    res.append(val)
                    left = True
            q = son
        return res
