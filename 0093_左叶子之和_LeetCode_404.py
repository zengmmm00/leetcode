# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        return self.dfs(root)

    def dfs(self, node, isLeft=False):
        if node.left is None and node.right is None:
            if isLeft == True:
                return node.val
            else:
                return 0
        else:
            s = 0
            if node.left is not None:
                s += self.dfs(node.left, isLeft=True)
            if node.right is not None:
                s += self.dfs(node.right, isLeft=False)
            return s
