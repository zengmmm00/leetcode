result = 0


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        global result
        result = 0
        _ = self.mergesort(nums)
        return result

    def mergesort(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return nums
        global result
        mid = int(len(nums) / 2)
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        ll = 0
        rr = 0
        new_nums = []
        while ll != len(left) or rr != len(right):
            if rr != len(right) and (ll == len(left) or right[rr] < left[ll]):
                result += len(left) - ll
                new_nums.append(right[rr])
                rr += 1
            else:
                new_nums.append(left[ll])
                ll += 1
        return new_nums


'''
二分法
'''
