class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0, 1]
        while True:
            l = len(res)
            for i in range(l):
                if len(res) == n + 1:
                    return res
                res.append(res[i] + 1)
