class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [False] * 1000001
        for i in nums:
            arr[i] = True
        for i in nums:
            k = target - i
            if 1 <= k <= 1000000 and arr[k] == True:
                return [i, k]
