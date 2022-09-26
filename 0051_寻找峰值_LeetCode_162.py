class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.binary(0, len(nums) - 1, nums)

    def binary(self, l, r, nums):
        if l < r:
            mid = int((l + r) / 2)
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return mid + 1
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    return mid - 1
            else:
                a = nums[mid - 1]
                b = nums[mid]
                c = nums[mid + 1]
                if b > a and b > c:
                    return mid
                elif a > b:
                    return self.binary(l, mid - 1, nums)
                else:
                    return self.binary(mid + 1, r, nums)
        else:
            return min(l, r)


'''
要判断mid在数组边界的情况
'''
