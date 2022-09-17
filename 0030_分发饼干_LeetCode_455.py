class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        j = 0
        res = 0
        if len(s) == 0:
            return res
        for i in range(len(g)):
            while s[j] < g[i]:
                j += 1
                if j == len(s):
                    return res
            # s[j] >= g[i]
            res += 1
            j += 1
            if j == len(s):
                return res
        return res
