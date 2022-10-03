class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, n, 0, 1, [], res)
        return res

    def dfs(self, k, n, s, j, sub, res):
        if len(sub) > k or s > n:
            return
        elif len(sub) == k and s == n:
            res.append(sub.copy())
        else:
            for i in range(j, 10):
                sub.append(i)
                self.dfs(k, n, s + i, i + 1, sub, res)
                sub.pop()
