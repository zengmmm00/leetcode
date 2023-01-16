# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dd, d = self.dfs(root)
        return max(dd, d)

    def dfs(self, node):
        if node is None:
            return 0, 0
        else:
            ldd, ld = self.dfs(node.left)
            rdd, rd = self.dfs(node.right)
            v = ld + rd
            return v, max(v, ldd + rdd + node.val)
