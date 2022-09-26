class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        global count
        count = 0
        if len(nums) == 0 or len(nums) == 1:
            return 0
        arr = self.mergeSort(nums)
        return count

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = int(len(arr) / 2)
            leftArr = self.mergeSort(arr[:mid])
            rightArr = self.mergeSort(arr[mid:])
            return self.merge(leftArr, rightArr)
        else:
            return arr

    def merge(self, leftArr, rightArr):
        global count
        l = 0
        r = 0
        arr = []
        while l < len(leftArr) or r < len(rightArr):
            if l == len(leftArr):
                arr += rightArr[r:]
                break
            elif r == len(rightArr):
                arr += leftArr[l:]
                break
            else:
                if leftArr[l] > rightArr[r]:
                    count += len(leftArr) - l
                    arr.append(rightArr[r])
                    r += 1
                else:
                    arr.append(leftArr[l])
                    l += 1
        return arr
