class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1:
            num = amount % coins[0]
            if num == 0:
                return int(amount / coins[0])
            else:
                return -1
        coins.sort()
        if coins[0] > amount:
            return -1
        dp = [0]
        for num in range(1, amount + 1):
            if num % coins[0] == 0:
                dp.append(num / coins[0])
            else:
                dp.append(-1)

        for i in range(1, len(coins)):
            item = coins[i]
            for num in range(item, amount + 1):
                if dp[num - item] != -1:
                    if dp[num] == -1:
                        dp[num] = dp[num - item] + 1
                    else:
                        dp[num] = min(dp[num], dp[num - item] + 1)

        return int(dp[-1])


'''
要处理特殊的amount。
注意dp为-1的情况。
dp要初始化。
'''
