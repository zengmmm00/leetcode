# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        q = [root]
        res = ''
        while len(q) != 0:
            node = q.pop(0)
            if node is not None:
                res += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res += 'null'
            res += ','
        res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        valStr = data.split(',')
        nodes = []
        for i in range(len(valStr)):
            if valStr[i] == 'null':
                nodes.append(TreeNode(-1001))
            else:
                val = int(valStr[i])
                nodes.append(TreeNode(val))
        n = len(nodes)
        root = nodes.pop(0)
        father = [root]
        while len(father) != 0:
            nextFa = []
            for i in range(len(father)):
                if len(nodes) == 0:
                    break
                son = nodes.pop(0)
                if son.val != -1001:
                    father[i].left = son
                    nextFa.append(son)
                if len(nodes) == 0:
                    break
                son = nodes.pop(0)
                if son.val != -1001:
                    father[i].right = son
                    nextFa.append(son)
            father = nextFa

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
