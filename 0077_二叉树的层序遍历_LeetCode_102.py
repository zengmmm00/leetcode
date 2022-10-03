# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []

        q = [root]
        while len(q) != 0:
            son = []
            val = []
            for node in q:
                if node is not None:
                    val.append(node.val)
                    son.append(node.left)
                    son.append(node.right)
            q = son
            if len(val) != 0:
                res.append(val)
        return res


'''
输出list[int]，而不是list[node]
'''
