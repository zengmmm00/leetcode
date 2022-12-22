class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = []
        # rob first
        for i in range(len(nums) - 1):
            if len(x) == 0 or nums[i] > x[-1]:
                x.append(nums[i])
            else:
                x.append(x[-1])
        for i in range(2, len(nums) - 1):
            for j in range(i, len(nums) - 1):
                x[j] = max(nums[j] + x[j - 2], x[j - 1], x[j])
        a = x[-1]

        # rob last
        x = []
        for i in range(0, len(nums)):
            if len(x) == 0:
                x.append(0)
            elif nums[i] > x[-1]:
                x.append(nums[i])
            else:
                x.append(x[-1])
        for i in range(2, len(nums)):
            for j in range(i, len(nums)):
                x[j] = max(nums[j] + x[j - 2], x[j - 1], x[j])
        b = x[-1]
        return max(a, b)
