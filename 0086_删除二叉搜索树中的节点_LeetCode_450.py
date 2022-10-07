# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        global k
        k = key
        if root is None:
            return None
        d, df = self.findKey(root, None)
        if d is None:
            return root
        root = self.delete(d, df, root)
        return root

    def delete(self, d, df, root):
        l = d.left
        r = d.right

        if l is None and r is None:
            if df is None:
                return None
            if df.left is d:
                df.left = None
            else:
                df.right = None
        elif r is None:
            if df is None:
                return l
            if df.left is d:
                df.left = l
            else:
                df.right = l
        else:
            if r.left is None:
                r.left = d.left
                if df is None:
                    return r
                if df.left is d:
                    df.left = r
                else:
                    df.right = r
            else:
                m, mf = self.noLeft(r.left, r)
                mf.left = m.right
                m.left = l
                m.right = r
                if df is None:
                    return m
                if df.left is d:
                    df.left = m
                else:
                    df.right = m

        return root

    def noLeft(self, node, father):
        if node.left is None:
            return (node, father)
        else:
            n, f = self.noLeft(node.left, node)
            return (n, f)

    def findKey(self, node, father):
        global k
        if node is None:
            return (None, father)
        if node.val == k:
            return (node, father)
        else:
            left, lf = self.findKey(node.left, node)
            if left is not None:
                return (left, lf)
            right, rf = self.findKey(node.right, node)
            return (right, rf)


'''
要考虑删掉root的情况
'''
