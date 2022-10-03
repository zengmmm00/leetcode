# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        _ = self.dfs(root, p, q, 0, res)
        return res[0]

    def dfs(self, node, p, q, count, res):
        if node is None:
            return count
        else:
            in_count = count
            if node.val == p.val or node.val == q.val:
                count += 1
            left = self.dfs(node.left, p, q, count, res)
            right = self.dfs(node.right, p, q, left, res)
            count = max(left, right)
            if in_count == 0 and count == 2 and len(res) == 0:
                res.append(node)
            return count
