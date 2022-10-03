class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island = [[0 for i in range(n)] for j in range(m)]
        k = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and island[i][j] == 0:
                    k += 1
                    q.append([i, j])
                    while len(q) != 0:
                        x, y = q.pop(0)
                        island[x][y] = k
                        if x - 1 >= 0 and island[x - 1][y] == 0 and grid[x - 1][y] == '1':
                            island[x - 1][y] = k
                            q.append([x - 1, y])
                        if x + 1 < m and island[x + 1][y] == 0 and grid[x + 1][y] == '1':
                            island[x + 1][y] = k
                            q.append([x + 1, y])
                        if y - 1 >= 0 and island[x][y - 1] == 0 and grid[x][y - 1] == '1':
                            island[x][y - 1] = k
                            q.append([x, y - 1])
                        if y + 1 < n and island[x][y + 1] == 0 and grid[x][y + 1] == '1':
                            island[x][y + 1] = k
                            q.append([x, y + 1])

        return k


'''
[[0 for i in range(n)] for j in range(m)] correct
[[0]*n for j in range(m)] correct
[[0]*n] * m wrong
用BFS遍历图
'''
