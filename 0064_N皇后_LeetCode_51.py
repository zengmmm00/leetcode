class Solution:
    def solveNQueens(self, n: int):
        global res
        res = []
        grid = []
        self.recall(0, n, grid)
        queen = []
        for i in range(len(res)):
            grid = res[i]
            queen.append([])
            for j in grid:
                s = '.' * j
                s += 'Q'
                s += '.' * (n - j - 1)
                queen[i].append(s)
        return queen

    def recall(self, i, n, grid):
        global res
        if i == n:
            res.append(grid.copy())
        else:
            for j in range(n):
                if i == 0 or self.check(i, j, grid):
                    grid.append(j)
                    self.recall(i + 1, n, grid)
                    grid.pop()

    def check(self, i, j, grid):
        if j in grid:
            return False
        for k in range(len(grid)):
            if i - k == abs(j - grid[k]):
                return False
        return True


'''
复制list要用.copy()
'''
