# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        global res
        res = []
        self.dfs(root, '')
        return res

    def dfs(self, node, sub):
        global res
        if node.left is None and node.right is None:
            res.append(sub + str(node.val))
            return
        if node.left is not None:
            self.dfs(node.left, sub + str(node.val) + '->')
        if node.right is not None:
            self.dfs(node.right, sub + str(node.val) + '->')
