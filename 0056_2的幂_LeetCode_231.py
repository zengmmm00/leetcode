class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(n):
            if 2 ** i == n:
                return True
            elif 2 ** i > n:
                return False


'''
math.log(x,base) 返回float类型，即使是结果应该整数也会带有小数，所以这题不能用math.log。
'''
