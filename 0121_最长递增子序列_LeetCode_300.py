class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        return max(dp)
