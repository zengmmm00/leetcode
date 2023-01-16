class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = []
        c = 0
        for n in nums:
            c += n
            s.append(c)
        ms = 0
        res = nums[0]
        for x in s:
            tmp = x - ms
            if tmp > res:
                res = tmp
            if x < ms:
                ms = x
        return res
