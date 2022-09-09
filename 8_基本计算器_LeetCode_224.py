class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '+' or c == '-' or c == '(':
                stack.append(c)
            elif c == ' ':
                continue
            elif c == ')':
                eq = []
                while stack[-1] != '(':
                    eq.insert(0, stack[-1])
                    stack.pop()
                stack.pop()
                stack.append(self.compute(eq))

            else:
                if len(stack) == 0 or str(stack[-1]) in '+-()':
                    stack.append(int(c))
                else:
                    stack[-1] = stack[-1] * 10 + int(c)
        return self.compute(stack)

    def compute(self, eq):
        result = 0
        while len(eq) != 0:
            item = eq.pop(0)
            if item == '-':
                result -= eq.pop(0)
            elif item == '+':
                result += eq.pop(0)
            else:
                result += item
        return result
