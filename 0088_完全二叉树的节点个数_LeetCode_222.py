# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # bfs
        if root is None:
            return 0
        count = 0
        q = [root]
        while len(q) != 0:
            node = q.pop(0)
            count += 1
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return count
