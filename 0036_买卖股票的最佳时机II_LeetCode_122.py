class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = -1
        for i in range(len(prices) - 1):
            if buy != -1:
                if prices[i] > prices[i + 1]:
                    res += prices[i] - buy
                    buy = -1
            else:
                if prices[i] < prices[i + 1]:
                    buy = prices[i]
        if buy != -1 and len(prices) > 0:
            res += prices[-1] - buy
        return res
