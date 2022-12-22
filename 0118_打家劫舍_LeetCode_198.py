class Solution:
    def rob(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            if len(x) == 0 or i > x[-1]:
                x.append(i)
            else:
                x.append(x[-1])
        for rob_num in range(2, len(nums) + 1):
            for house in range(rob_num, len(nums)):
                x[house] = max([nums[house] + x[house - 2], x[house], x[house - 1]])
        return x[-1]
