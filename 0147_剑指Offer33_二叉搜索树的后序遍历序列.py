class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.divide(postorder)

    def divide(self, order):
        if len(order) == 0:
            return True
        root = order.pop()
        k = -1
        for i in range(len(order)):
            if order[i] < root:
                k = i
            else:
                break
        for i in range(k + 1, len(order)):
            if order[i] < root:
                return False
        left = True
        right = True
        if k != -1:
            left = self.divide(order[:k + 1])
        if k != len(order) - 1:
            right = self.divide(order[k + 1:])
        return left and right
