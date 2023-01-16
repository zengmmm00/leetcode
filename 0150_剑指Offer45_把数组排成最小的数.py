import functools


def cmp(a, b):
    sa = str(a)
    sb = str(b)
    x = int(sa + sb)
    y = int(sb + sa)
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=functools.cmp_to_key(cmp))
        res = ''
        for num in nums:
            res += str(num)
        return res
