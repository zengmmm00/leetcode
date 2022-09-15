class Oj:
    def __init__(self, i, v, c):
        self.index = i
        self.val = v
        self.count = c


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)

        arr = [Oj(x, nums[x], 0) for x in range(len(nums))]  # id, val, count
        self.mergeSort(arr, 0, len(nums) - 1)

        for i in range(len(arr)):
            count[arr[i].index] = arr[i].count
        return count

    def mergeSort(self, arr, p, q):
        if p < q:
            mid = int((p + q) / 2)
            self.mergeSort(arr, p, mid)
            self.mergeSort(arr, mid + 1, q)
            self.merge(arr, p, q, mid)

    def merge(self, arr, p, q, mid):
        l = 0
        r = 0
        lArr = arr[p:mid + 1]
        rArr = arr[mid + 1:q + 1]
        for i in range(p, q + 1):
            if l == len(lArr):
                arr[i] = rArr[r]
                r += 1
            elif r == len(rArr):
                lArr[l].count += r
                arr[i] = lArr[l]
                l += 1
            else:
                if lArr[l].val <= rArr[r].val:
                    lArr[l].count += r
                    arr[i] = lArr[l]
                    l += 1
                else:
                    arr[i] = rArr[r]
                    r += 1


'''
用归并排序。
在左边的元素放入array的时候更新count，加上右边已放入array的元素的个数。
'''