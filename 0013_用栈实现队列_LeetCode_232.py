class MyQueue:

    def __init__(self):
        self.s1 = []
        # s2 = []
        self.num = 0

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.num += 1

    def pop(self) -> int:
        out = self.s1[0]
        del self.s1[0]
        self.num -= 1
        return out

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return self.num == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
