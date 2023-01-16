class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums) / 2
        target = int(s)
        if target != s:
            return False
        dp = [False] * (target + 1)

        for i in range(len(nums)):
            ndp = [False]
            for j in range(1, target + 1):
                if dp[j] is True:
                    ndp.append(True)
                else:
                    if j - nums[i] == 0:
                        ndp.append(True)
                    elif j - nums[i] >= 1:
                        ndp.append(dp[j - nums[i]])
                    else:
                        ndp.append(False)
            if ndp[target] is True:
                return True
            dp = ndp
        return False
