# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
count = 0


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        global count
        count = 0
        return self.getVal(root, k).val

    def getVal(self, node, k):
        global count
        if node is None:
            return None
        else:
            right = self.getVal(node.right, k)
            if right is not None:
                return right
            count += 1
            if count == k:
                return node
            left = self.getVal(node.left, k)
            if left is not None:
                return left
            return None
