class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s)):
                if j + i > len(s):
                    break
                sub = s[j:j + i]
                if i % 2 == 0 and sub[0:int(i / 2)][::-1] == sub[int(i / 2):i]:
                    return sub
                elif i % 2 == 1 and sub[0:int(i / 2)][::-1] == sub[int(i / 2) + 1:i]:
                    return sub
        return s[0]
