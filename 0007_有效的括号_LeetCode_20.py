class Solution:
    def isValid(self, s: str) -> bool:
        openb = '([{'
        closeb = ')]}'
        stack = []
        for c in s:
            closeid = closeb.find(c)
            if closeid == -1:  # open
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                openid = openb.find(stack[-1])
                if closeid != openid:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True


'''
最后要检查stack中是否有剩余符号。
'''
