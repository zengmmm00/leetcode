class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if len(array) == 0:
            return [-1, -1]
        a = 0
        for i in range(len(array)):
            if i == len(array) - 1:
                return [-1, -1]
            if array[i] > array[i + 1]:
                a = i + 1
                break
        b = 0
        for i in range(len(array) - 1, 0, -1):
            if array[i] < array[i - 1]:
                b = i - 1
                break
        if a < b:
            mini = min(array[a:b + 1])
            maxi = max(array[a:b + 1])
        else:
            mini = min(array[b:a + 1])
            maxi = max(array[b:a + 1])

        c = 0
        for i in range(a - 1, -1, -1):
            if array[i] <= mini:
                c = i + 1
                break
        d = len(array) - 1
        for i in range(b + 1, len(array)):
            if array[i] >= maxi:
                d = i - 1
                break
        return [c, d]
