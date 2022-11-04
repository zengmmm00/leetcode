class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums.reverse()
        dp = [nums[0]]
        for i in range(1, len(nums)):
            start_num = nums[i]
            s = max(start_num, start_num + dp[-1])
            dp.append(s)
        return max(dp)
