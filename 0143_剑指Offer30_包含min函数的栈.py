class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.m) == 0:
            self.m.append(x)
        else:
            if self.m[-1] < x:
                self.m.append(self.m[-1])
            else:
                self.m.append(x)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()
            self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
