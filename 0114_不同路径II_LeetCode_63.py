class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        x = []
        ob = -1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                ob = i
                break
        if ob == -1:
            x = [1] * n
        else:
            for i in range(ob):
                x.append(1)
            for i in range(ob, n):
                x.append(0)

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                x[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    x[j] = 0
                else:
                    x[j] += x[j - 1]
        return x[-1]
