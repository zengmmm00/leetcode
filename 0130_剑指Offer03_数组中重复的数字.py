class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = [0] * len(nums)
        for i in nums:
            if d[i] == 0:
                d[i] = 1
            else:
                return i
