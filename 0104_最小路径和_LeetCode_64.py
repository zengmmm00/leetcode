class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dis_old = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            dis_new = []
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    p = min(dis_new[-1], dis_old[j])
                elif i - 1 >= 0:
                    p = dis_old[j]
                elif j - 1 >= 0:
                    p = dis_new[-1]
                else:
                    p = 0
                dis_new.append(p + grid[i][j])
            dis_old = dis_new
        return dis_old[-1]
