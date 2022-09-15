class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[m + n - i - 1] = nums1[m - i - 1]

        p1 = n  # ->m+n
        p2 = 0  # ->n
        for i in range(m + n):
            if p1 == m + n:
                nums1[i] = nums2[p2]
                p2 += 1
            elif p2 == n:
                nums1[i] = nums1[p1]
                p1 += 1
            else:
                if nums1[p1] <= nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 += 1
                else:
                    nums1[i] = nums2[p2]
                    p2 += 1


'''
nums1 = nums1[m:m+n] + nums1[0:m]会改变nums1的地址
'''
