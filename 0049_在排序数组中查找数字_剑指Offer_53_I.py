class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        f = False
        for i in range(len(nums)):
            if nums[i] == target:
                count += 1
                f = True
            else:
                if f:
                    return count
        return count
