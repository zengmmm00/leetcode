# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.dfs(nums)
        return root

    def dfs(self, arr):
        if len(arr) == 0:
            return None
        else:
            m = int(len(arr) / 2)
            mid = TreeNode(arr[m])
            left = self.dfs(arr[:m])
            right = self.dfs(arr[m + 1:])
            mid.left = left
            mid.right = right
            return mid
