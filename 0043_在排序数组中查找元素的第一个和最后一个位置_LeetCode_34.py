class Ob:
    def __init__(self, i, v):
        self.index = i
        self.num = 1
        self.value = v


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        obNums = []
        lastNum = -1000000001
        for i in range(len(nums)):
            if nums[i] != lastNum:
                obNums.append(Ob(i, nums[i]))
            else:
                obNums[-1].num += 1

            lastNum = nums[i]
        return self.binary(0, len(obNums) - 1, obNums, target)

    def binary(self, a, b, obNums, target):
        if a > b:
            return [-1, -1]
        mid = int((a + b) / 2)
        ob = obNums[mid]
        if ob.value == target:
            return [ob.index, ob.index + ob.num - 1]
        elif ob.value > target:
            return self.binary(a, mid - 1, obNums, target)
        else:
            return self.binary(mid + 1, b, obNums, target)
