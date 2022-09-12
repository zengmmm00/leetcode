class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        l = len(height)
        for h in height:
            if len(stack) == 0:
                if h != 0:
                    stack.append(h)
            else:
                if h <= stack[-1]:
                    stack.append(h)
                else:
                    if h >= stack[0]:
                        res += stack[0] * len(stack) - sum(stack)
                        while len(stack) != 0:
                            stack.pop()
                        stack.append(h)
                    else:
                        out = []
                        while stack[-1] < h:
                            out.append(stack.pop())
                        res += h * len(out) - sum(out)
                        stack += [h] * (len(out) + 1)
        return res
