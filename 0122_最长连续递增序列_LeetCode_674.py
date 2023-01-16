class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp.append(dp[-1] + 1)
            else:
                dp.append(1)
        return max(dp)
