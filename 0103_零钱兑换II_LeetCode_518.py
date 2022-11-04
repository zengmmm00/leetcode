class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        coins.sort()
        dp = [0] * (amount + 1)
        v = coins[0]
        dp[0] = 1
        for j in range(v, amount + 1):
            if j % v == 0:
                dp[j] = 1

        for i in range(1, len(coins)):
            v = coins[i]
            if v > amount:
                break
            for j in range(v, amount + 1):
                dp[j] = dp[j] + dp[j - v]

        return dp[-1]


'''
需要用第一个数值初始化dp数组，之后遍历时要跳过初始化用的数值
'''
