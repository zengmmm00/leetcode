class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zeros = nums.count(0)
        nums = nums[zeros:]
        for i in range(1, len(nums)):
            empty = nums[i] - nums[i - 1]
            if empty == 0:
                return False
            if empty > 1:
                zeros -= empty - 1
                if zeros < 0:
                    return False

        return True
