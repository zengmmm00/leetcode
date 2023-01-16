class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return 1
        dp = [0]
        for i in range(1, len(s)):
            n = int(s[i - 1] + s[i])
            if n < 26 and s[i - 1] != '0':
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])
        result = 1 + dp[-1]
        i = 3
        while i < len(s):
            ndp = [0] * i
            for j in range(i, len(s)):
                n = int(s[j - 1] + s[j])
                if n < 26 and s[j - 1] != '0':
                    ndp.append(dp[j - 2])
                    result += dp[j - 2]
                else:
                    ndp.append(ndp[-1])
            dp = ndp
            i += 2
        return result

'''
比较0和'0'
'''