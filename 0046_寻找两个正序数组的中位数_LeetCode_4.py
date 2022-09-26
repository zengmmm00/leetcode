class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = 2 * m
        leftMax1 = 0
        leftMax2 = 0
        rightMin1 = 0
        rightMin2 = 0

        while left <= right:
            cut1 = left + int((right - left) / 2)
            cut2 = m + n - cut1

            if cut1 == 0:
                leftMax1 = -1000001
            else:
                leftMax1 = nums1[int((cut1 - 1) / 2)]
            if cut2 == 0:
                leftMax2 = -1000001
            else:
                leftMax2 = nums2[int((cut2 - 1) / 2)]

            if cut1 == 2 * m:
                rightMin1 = 1000001
            else:
                rightMin1 = nums1[int((cut1) / 2)]

            if cut2 == 2 * n:
                rightMin2 = 1000001
            else:
                rightMin2 = nums2[int((cut2) / 2)]

            if leftMax1 > rightMin2:
                right = cut1 - 1
            elif leftMax2 > rightMin1:
                left = cut1 + 1
            else:
                break
        return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2.0
'''

'''