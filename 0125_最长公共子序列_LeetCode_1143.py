class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            tmp = text1
            text1 = text2
            text2 = tmp
        dp = []
        count = 0
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                count = 1
            dp.append(count)
        for i in range(1, len(text2)):
            ndp = dp.copy()
            if text2[i] == text1[0]:
                ndp[0] = 1
            else:
                ndp[0] = dp[0]
            for j in range(1, len(text1)):
                if text2[i] == text1[j]:
                    ndp[j] = dp[j - 1] + 1
                else:
                    ndp[j] = max(ndp[j - 1], dp[j])
            dp = ndp
        return dp[-1]
