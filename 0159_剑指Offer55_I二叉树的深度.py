# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, d):
        if node is None:
            return d
        else:
            left = self.dfs(node.left, d + 1)
            right = self.dfs(node.right, d + 1)
            return max(left, right)
