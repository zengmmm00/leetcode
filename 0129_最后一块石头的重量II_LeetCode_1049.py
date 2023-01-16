class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones = sorted(stones)
        s = sum(stones)
        neg = int(s / 2)
        dp = []
        for i in range(neg + 1):
            if i >= stones[0]:
                dp.append(stones[0])
            else:
                dp.append(0)
        for i in range(1, len(stones)):
            ndp = dp.copy()
            for j in range(stones[i], neg + 1):
                ndp[j] = max(ndp[j], dp[j - stones[i]] + stones[i])
            dp = ndp
        return s - dp[-1] * 2

# 01背包
