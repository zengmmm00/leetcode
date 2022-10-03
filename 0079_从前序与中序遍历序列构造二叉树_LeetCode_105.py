# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root = None
        val2node = dict()
        for val in preorder:
            val2node[val] = TreeNode(val)
        self.dfs(inorder, preorder, val2node)
        return val2node[preorder[0]]

    def dfs(self, sub_in, sub_pre, val2node):
        if len(sub_pre) == 0:
            return
        else:
            root = val2node[sub_pre[0]]
            root_id = sub_in.index(root.val)
            left_in = sub_in[:root_id]
            right_in = sub_in[root_id + 1:]
            left_pre = sub_pre[1:root_id + 1]
            right_pre = sub_pre[root_id + 1:]
            if len(left_pre) != 0:
                root.left = val2node[left_pre[0]]

            if len(right_pre) != 0:
                root.right = val2node[right_pre[0]]

            self.dfs(left_in, left_pre, val2node)
            self.dfs(right_in, right_pre, val2node)
