# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global m
        m = 100001
        a, b = self.traverse(root)
        return m

    def traverse(self, node):
        global m
        a = node
        b = node
        if node.left is not None:
            ll, lr = self.traverse(node.left)
            m = min(m, abs(node.val - lr.val))
            a = ll
        if node.right is not None:
            rl, rr = self.traverse(node.right)
            m = min(m, abs(node.val - rl.val))
            b = rr
        return a, b


'''
最小绝对差不一定是父节点和子节点之间的。
'''
