class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        a = s[:n]
        if n < len(s):
            b = s[n:]
        else:
            b = ''
        return b + a
