# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        node = root
        newRoot = None
        while node is not None:
            if low <= node.val <= high:
                newRoot = node
                break
            elif node.val < low:
                node = node.right
            else:
                node = node.left
        if newRoot is None:
            return None
        else:
            self.delNode(newRoot, low, high)
        return newRoot

    def delNode(self, node, low, high):
        # node can not be None
        nl = node.left
        nr = node.right
        while nl is not None and nl.val < low:
            node.left = nl.right
            nl = nl.right
        if nl is not None:
            self.delNode(nl, low, high)
        while nr is not None and nr.val > high:
            node.right = nr.left
            nr = nr.left
        if nr is not None:
            self.delNode(nr, low, high)
