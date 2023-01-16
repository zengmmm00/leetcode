class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict()
        s = sum(nums)
        if nums[0] == 0:
            dp[0] = 2
        else:
            dp[-nums[0]] = 1
            dp[nums[0]] = 1

        for i in range(1, len(nums)):
            num = nums[i]
            ndp = dict()
            if num == 0:
                for k, v in dp.items():
                    ndp[k] = dp[k] * 2
            else:
                for k, v in dp.items():
                    if k - num not in ndp.keys():
                        ndp[k - num] = dp[k]
                    else:
                        ndp[k - num] = ndp[k - num] + dp[k]
                    if k + num not in ndp.keys():
                        ndp[k + num] = dp[k]
                    else:
                        ndp[k + num] = ndp[k + num] + dp[k]
            dp = ndp
        if target in dp.keys():
            return dp[target]
        else:
            return 0
