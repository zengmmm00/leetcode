class CQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if len(self.a) == 0:
            return -1
        else:
            n = len(self.a)
            for i in range(n):
                self.b.append(self.a.pop())
            x = self.b.pop()
            for i in range(n - 1):
                self.a.append(self.b.pop())
            return x

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
