# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        global f
        f = True
        _ = self.dfs(root)
        return f

    def dfs(self, node, depth=0):
        global f
        if node is None:
            return depth
        else:
            l = self.dfs(node.left, depth + 1)
            r = self.dfs(node.right, depth + 1)
            if abs(l - r) > 1:
                f = False
            return max(l, r)


'''
height-balanced binary tree: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
