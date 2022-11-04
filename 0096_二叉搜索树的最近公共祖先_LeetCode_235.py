# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        walk = dict()
        self.traverse(root, walk)
        self.findP(root, p, walk)
        global ans
        ans = p
        self.findQ(root, q, walk)
        return ans

    def findP(self, node, p, walk):
        if node is None:
            return
        else:
            walk[node.val] = True
            if node.val == p.val:
                return
            elif p.val < node.val:
                self.findP(node.left, p, walk)
            else:
                self.findP(node.right, p, walk)

    def findQ(self, node, q, walk):
        global ans

        if node is None:
            return
        else:
            if not walk[node.val]:
                return
            else:
                ans = node
                if q.val == node.val:
                    return
                elif q.val < node.val:
                    self.findQ(node.left, q, walk)
                else:
                    self.findQ(node.right, q, walk)

    def traverse(self, node, walk):
        if node is None:
            return
        else:
            walk[node.val] = False
            self.traverse(node.left, walk)
            self.traverse(node.right, walk)
