class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums) - 1, nums, target)

    def binary(self, a, b, nums, target):
        if a > b:
            return -1
        mid = int((a + b) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary(a, mid - 1, nums, target)
        else:
            return self.binary(mid + 1, b, nums, target)
