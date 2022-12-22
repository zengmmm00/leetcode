class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        m = 0
        for i in range(len(prices) - 1, -1, -1):
            p = prices[i]
            m = max(m, p)
            res = max(res, m - p)
        return res
