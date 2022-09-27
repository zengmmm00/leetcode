class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b = x ^ y
        s = str(bin(b))[2:]
        res = 0
        for c in s:
            res += int(c)
        return res


'''
bin() 十进制转二进制
^ 异或
'''
