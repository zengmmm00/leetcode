class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                x[j] += x[j - 1]
        return x[n - 1]
