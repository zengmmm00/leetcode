from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        way = 0
        for twoNum in range(int(n / 2) + 1):
            oneNum = n - 2 * twoNum
            way += factorial(oneNum + twoNum) / (factorial(oneNum) * factorial(twoNum))
        return int(way)
