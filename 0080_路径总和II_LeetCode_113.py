# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return []

        self.dfs(res, root, [], 0, targetSum)
        return res

    def dfs(self, res, node, sub, s, targetSum):
        s += node.val
        if node.left is None and node.right is None:
            if s == targetSum:
                res.append(sub + [node.val])
            else:
                return
        else:
            if node.left is not None:
                self.dfs(res, node.left, sub + [node.val], s, targetSum)
            if node.right is not None:
                self.dfs(res, node.right, sub + [node.val], s, targetSum)


'''
如果dfs结束的条件是node is None，然后再添加path，会导致每条path被添加两次，因为leaf的left和right都是None。
'''
