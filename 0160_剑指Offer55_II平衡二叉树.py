# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
flag = True


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        global flag
        flag = True
        _ = self.dfs(root, 0)
        return flag

    def dfs(self, node, d):
        global flag

        if node is None:
            return d
        else:
            left = self.dfs(node.left, d + 1)
            right = self.dfs(node.right, d + 1)
            if abs(left - right) > 1:
                flag = False
            return max(left, right)
