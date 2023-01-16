class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs = s[::-1]
        dp = []
        count = 0
        for i in range(len(s)):
            if s[i] == rs[0]:
                count = 1
            dp.append(count)
        for i in range(1, len(rs)):
            ndp = []
            if rs[i] == s[0]:
                ndp.append(1)
            else:
                ndp.append(max(0, dp[0]))
            for j in range(1, len(s)):
                if rs[i] == s[j]:
                    ndp.append(dp[j - 1] + 1)
                else:
                    ndp.append(max(dp[j], ndp[j - 1]))
            dp = ndp
        return dp[-1]
