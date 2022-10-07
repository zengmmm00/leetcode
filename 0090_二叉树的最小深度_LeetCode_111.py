# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root)

    def dfs(self, node, depth=1):
        if node.left is None and node.right is None:
            return depth
        elif node.left is None and node.right is not None:
            return self.dfs(node.right, depth + 1)
        elif node.left is not None and node.right is None:
            return self.dfs(node.left, depth + 1)
        else:
            r = self.dfs(node.right, depth + 1)
            l = self.dfs(node.left, depth + 1)
            return min(r, l)
