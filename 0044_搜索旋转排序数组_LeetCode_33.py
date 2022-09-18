class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 1:
            return nums[0] == target
        k = self.findK(0, len(nums) - 1, nums)
        return self.binary(0, len(nums) - 1, nums, target, k)

    def binary(self, a, b, nums, target, k):
        if a > b:
            return -1
        mid = int((a + b) / 2)
        rm = self.getReal(mid, k, len(nums))
        if nums[rm] == target:
            return rm

        elif nums[rm] > target:
            return self.binary(a, mid - 1, nums, target, k)
        else:
            return self.binary(mid + 1, b, nums, target, k)

    def getReal(self, i, k, n):
        # if k == 0:
        #     return i
        return (i + k + 1) % n

    def findK(self, a, b, nums):
        mid = int((a + b) / 2)
        if b < 0:
            return -1
        if a >= len(nums) or mid == len(nums) - 1:
            return len(nums) - 1
        if nums[mid] > nums[mid + 1]:
            return mid
        elif nums[a] == nums[mid]:
            return -1
        elif nums[a] < nums[mid]:
            return self.findK(mid, b, nums)
        else:
            return self.findK(a, mid, nums)


'''
k可能为0（没有逆序数）
'''
