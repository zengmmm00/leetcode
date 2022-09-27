class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.binary(0, len(arr) - 1, arr)

    def binary(self, a, b, arr):
        m = int((a + b) / 2)
        if m == 0:
            if arr[m] > arr[m + 1]:
                return m
            else:
                return m + 1
        if m == len(arr) - 1:
            if arr[m] > arr[m - 1]:
                return m
            else:
                return m - 1
        l = arr[m - 1]
        r = arr[m + 1]
        x = arr[m]
        if x > l and x > r:
            return m
        elif l > x > r:
            return self.binary(a, m - 1, arr)
        else:
            return self.binary(m + 1, b, arr)
