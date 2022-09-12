class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        in_stack = dict()
        for i in popped:
            in_stack[i] = False
        stack = []
        for out in popped:
            while in_stack[out] is False:
                if len(pushed) == 0:
                    return False
                else:
                    num = pushed.pop(0)
                    stack.append(num)
                    in_stack[num] = True
            if len(stack) == 0:
                return False
            elif stack[-1] == out:
                del stack[-1]
                in_stack[out] = False
            else:
                return False
        return True
