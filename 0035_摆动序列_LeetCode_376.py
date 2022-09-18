class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        while len(nums) >= 2:
            if nums[0] == nums[1]:
                nums.pop(0)
            else:
                break
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        if nums[0] < nums[1]:
            pos = False
        else:
            pos = True
        p = 1
        res = 2
        while p < len(nums) - 1:
            if pos:
                if nums[p + 1] > nums[p]:
                    res += 1
                    pos = False
                    p += 1
                else:
                    p += 1
            else:
                if nums[p + 1] < nums[p]:
                    res += 1
                    pos = True
                    p += 1
                else:
                    p += 1
        return res
