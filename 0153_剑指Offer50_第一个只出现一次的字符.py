class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            count[i] += 1

        for c in s:
            i = ord(c) - ord('a')
            if count[i] == 1:
                return c
        return ' '
