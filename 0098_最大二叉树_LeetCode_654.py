# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        sortNums = sorted(nums, reverse=True)
        seq = dict()
        for i in range(len(nums)):
            seq[nums[i]] = i
        root = TreeNode(sortNums.pop(0))
        self.traverse(root, seq, sortNums)
        return root

    def traverse(self, node, seq, sortNums):
        left = []
        right = []
        while len(sortNums) != 0:
            n = sortNums.pop(0)
            if seq[n] > seq[node.val]:
                right.append(n)
            else:
                left.append(n)
        if len(left) != 0:
            node.left = TreeNode(left.pop(0))
            self.traverse(node.left, seq, left)
        if len(right) != 0:
            node.right = TreeNode(right.pop(0))
            self.traverse(node.right, seq, right)
