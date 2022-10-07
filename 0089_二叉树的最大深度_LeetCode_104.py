# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node, depth=0):
        if node is None:
            return depth
        else:
            l = self.dfs(node.left, depth + 1)
            r = self.dfs(node.right, depth + 1)
            return max(l, r)
