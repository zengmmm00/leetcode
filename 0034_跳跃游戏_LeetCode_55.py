class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        a = len(nums) - 1
        b = len(nums) - 2
        while b != -1:
            if a - b <= nums[b]:
                a = b
            b -= 1
        if a == 0:
            return True
        return False
