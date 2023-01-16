class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = []
        res = 0
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp.append(1)
                res = 1
            else:
                dp.append(0)
        for i in range(1, len(nums2)):
            ndp = []
            for j in range(len(nums1)):
                if nums1[j] != nums2[i]:
                    ndp.append(0)
                else:
                    if j == 0:
                        ndp.append(1)
                    else:
                        ndp.append(dp[j - 1] + 1)
            res = max(res, max(ndp))
            dp = ndp
        return res
