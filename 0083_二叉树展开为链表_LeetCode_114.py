# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        a, b = self.dfs(root)

    def dfs(self, node):
        if node.left is None and node.right is None:
            return (node, node)
        else:
            left = node.left
            node.left = None
            right = node.right
            node.right = None
            if left is not None and right is not None:
                la, lb = self.dfs(left)
                ra, rb = self.dfs(right)
                node.right = la
                lb.right = ra
                return (node, rb)
            if left is None and right is not None:
                ra, rb = self.dfs(right)
                node.right = ra
                return (node, rb)
            if left is not None and right is None:
                la, lb = self.dfs(left)
                node.right = la
                return (node, lb)
