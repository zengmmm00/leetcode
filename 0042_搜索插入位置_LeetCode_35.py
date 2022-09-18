class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums) - 1, nums, target)

    def binary(self, a, b, nums, target):
        mid = int((a + b) / 2)
        if nums[mid] == target:
            return mid
        else:
            if a >= b:
                if target > nums[mid]:
                    return mid + 1
                else:
                    return mid
            else:
                if nums[mid] > target:
                    return self.binary(a, mid - 1, nums, target)
                else:
                    return self.binary(mid + 1, b, nums, target)


'''
判断是否要insert的条件是a>=b。
int((0-1) / 2) =0
'''
