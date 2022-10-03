class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, res, 1, [], 1)
        return res

    def dfs(self, n, k, res, d, sub, j):
        if d > k:
            res.append(sub.copy())
            return
        else:
            for i in range(j, n + 1):
                sub.append(i)
                self.dfs(n, k, res, d + 1, sub, i + 1)
                sub.pop()
