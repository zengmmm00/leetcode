# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        else:
            return self.binary(1, n)

    def binary(self, a, b):
        m = int((a + b) / 2)
        if not isBadVersion(m):
            return self.binary(m + 1, b)
        else:
            if not isBadVersion(m - 1):
                return m
            else:
                return self.binary(a, m - 1)
