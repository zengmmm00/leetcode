# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global res
        res = 0
        # if root is None:
        # return 0
        self.backtracking(root, targetSum, 0, False)
        return res

    def backtracking(self, node, target, s, pick):
        global res
        # if len(nodes) == 0:
        # return

        if node is None:
            return

        if pick is False:
            # do not add current, go left
            self.backtracking(node.left, target, s, False)
            # do not add current, go right
            self.backtracking(node.right, target, s, False)

        if s + node.val == target:
            res += 1

        # add current, go left
        self.backtracking(node.left, target, s + node.val, True)
        # add current, go right
        self.backtracking(node.right, target, s + node.val, True)


'''
即使加上此时的node.val的和为target，也要继续往下走，因为可能这样的path：1，-2，1，-1
'''
