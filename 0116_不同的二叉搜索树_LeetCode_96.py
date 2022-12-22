class Solution:
    def numTrees(self, n: int) -> int:
        x = dict()
        x[1] = 1
        x[0] = 1
        for i in range(2, n + 1):
            count = 0
            for j in range(1, i + 1):
                left = j - 1
                right = i - 1 - left
                count += x[left] * x[right]
            x[i] = count
        return x[n]
