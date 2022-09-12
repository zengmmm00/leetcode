class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0 for _ in range(len(T))]
        for index, value in enumerate(T):
            while stack and T[stack[-1]] < value:
                pop_index = stack.pop()
                res[pop_index] = index - pop_index
            stack.append(index)
        return res


'''
用单独递增栈
'''
