class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res
