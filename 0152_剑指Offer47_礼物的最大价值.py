class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        s = 0
        dp = []
        for i in grid[0]:
            s += i
            dp.append(s)
        for i in range(1, len(grid)):
            row = grid[i]
            dp[0] += row[0]
            for j in range(1, len(row)):
                dp[j] = max(dp[j], dp[j - 1]) + row[j]
        return dp[-1]
