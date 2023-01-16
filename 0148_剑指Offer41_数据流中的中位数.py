class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        n = len(self.nums)
        flag = True
        for i in range(n):
            if self.nums[i] > num:
                self.nums.insert(i, num)
                flag = False
                break
        if flag:
            self.nums.append(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[int(n / 2)]
        else:
            return (self.nums[int(n / 2)] + self.nums[int(n / 2) - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
