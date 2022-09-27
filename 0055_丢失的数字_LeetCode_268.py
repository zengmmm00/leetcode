class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = [True] * (len(nums) + 1)
        for n in nums:
            miss[n] = False
        return miss.index(True)


'''
<list_name>.index(): 查找某个数的位置
'''
