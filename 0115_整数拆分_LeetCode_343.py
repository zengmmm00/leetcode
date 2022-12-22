class Solution:
    def integerBreak(self, n: int) -> int:
        x = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                a = j - i
                x[j] = max([x[j], x[a] * i, a * i])
        return x[-1]
