# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global s
        s = 0
        if root is None:
            return None
        self.getSum(root)
        _ = self.dfs(root, s)
        return root

    def dfs(self, node, remain):
        if node is None:
            return remain
        else:
            left = self.dfs(node.left, remain)
            v = node.val
            node.val = left
            right = self.dfs(node.right, left - v)
            return right

    def getSum(self, node):
        global s
        if node is None:
            return
        else:
            s += node.val
            self.getSum(node.left)
            self.getSum(node.right)
