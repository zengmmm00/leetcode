class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                a += 1
            elif nums[i] == 1:
                b += 1
            else:
                c += 1
        for i in range(a):
            nums[i] = 0
        for i in range(a, a + b):
            nums[i] = 1
        for i in range(a + b, a + b + c):
            nums[i] = 2
