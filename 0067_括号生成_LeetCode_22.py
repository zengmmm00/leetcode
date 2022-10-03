class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtracking(n, 0, [], res, 0, 0)
        return res

    def backtracking(self, n, d, sub, res, a, b):
        if a > n or b > n or b > a:
            return
        elif d == 2 * n:
            s = ''.join(sub)
            res.append(s)
        else:
            # put (
            sub.append('(')
            self.backtracking(n, d + 1, sub, res, a + 1, b)
            sub.pop()

            # put )
            sub.append(')')
            self.backtracking(n, d + 1, sub, res, a, b + 1)
            sub.pop()
