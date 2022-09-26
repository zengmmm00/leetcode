class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            for j in range(i + 1, len(nums) - 1):
                if nums[j] == 0:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[k] == 0:
                        continue
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
        return count

'''
sorted后要重新赋值
'''