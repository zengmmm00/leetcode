class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.f, self.r, self.k = 0, 0, k

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            n = self.f
        else:
            n = (self.f - 1 + self.k) % self.k
        if self.q[n] != -1:
            return False
        self.f = n
        self.q[n] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            n = self.r
        else:
            n = (self.r + 1) % self.k
        if self.q[n] != -1:
            return False
        self.r = n
        self.q[n] = value
        return True

    def deleteFront(self) -> bool:
        if self.q[self.f] == -1:
            return False
        self.q[self.f] = -1
        if not self.isEmpty():
            n = (self.f + 1) % self.k
            self.f = n
        return True

    def deleteLast(self) -> bool:
        if self.q[self.r] == -1:
            return False
        self.q[self.r] = -1
        if not self.isEmpty():
            n = (self.r - 1 + self.k) % self.k
            self.r = n
        return True

    def getFront(self) -> int:
        return self.q[self.f]

    def getRear(self) -> int:
        return self.q[self.r]

    def isEmpty(self) -> bool:
        if self.q[self.f] == -1 and self.q[self.r] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        if self.isEmpty():
            n = self.r
        else:
            n = (self.r + 1) % self.k
        if self.q[n] != -1:
            return True
        return False


'''
插入、删除前都要判断是否环形队列是否为空。
'''
