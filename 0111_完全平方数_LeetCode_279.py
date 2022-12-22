class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        sq = []
        for i in range(1, n):
            if i ** 2 > n:
                break
            else:
                sq.append(i ** 2)
        x = [i for i in range(n + 1)]
        for i in sq:
            for j in range(i, n + 1):
                a = j // i
                b = j % i
                if a + x[b] < x[j]:
                    x[j] = a + x[b]
        return x[-1]
